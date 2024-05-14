import numpy as np
import math
from scipy.stats import binom


class WPR:

    def __init__(self,
                 A,
                 W,
                 gamma: float,
                 theta: float,
                 alpha: float,
                 initial_conditions_infected: np.ndarray,
                 ) -> None:

        '''
        Constructor:
        Assumptions: - at each time steps, in each airport, there is a number of people equal to the number of arriving routes*100: constant number along the algorithm
                     - number of new infected people: binomial r.v.: n is the total number of trial, p the probability that we have a success in a single trial:
                                                      - n is the number of non-sick people in the airport at the beginning of the time step (only non infected people can be infected)
                                                      - p is a function of the number of already infected people (deterministic function, proportional to the proportion of already infected people right now)

        Algorithm relays on the paper, with a difference: beta_i varies along the algorithm: Markov chain is  ot homogeneus anymore: relays

        :param A: adjacency matrix
        :param W: weights matrix
        :param gamma: teleportation parameter ([0,1)): in this case, has to be as high as possible: not dead ends in the graph (?)
        :param theta: trade-off degree-weight parameter ([0,1]): in this case, has to be as high as possible: number of flights are more important than number of connections
        :param alpha: parameter of the convex combination for evaluating beta_i: has to be low in order to give more importance to the infection parameter
        :param initial_conditions_infected: number of infected in each airport at time 0
        '''

        if A.shape != W.shape:
            raise ValueError('A and W need to have the same dimensions')
        if gamma < 0 or gamma >= 1:
            raise ValueError('Gamma has to be in [0,1)')
        if theta < 0 or theta > 1:
            raise ValueError('Theta has to be in [0,1]')
        if alpha < 0 or alpha > 1:
            raise ValueError('Alpha has to be in [0,1]')

        self.A = A
        self.W = W
        self.n_airports = A.shape[0]                                        #how many airports
        self.ranks = np.ones(self.n_airports)                               #at the beginning, all the airports have the same rank

        self.degree_out = [sum(A[i, :]) for i in range(self.n_airports)]    #degree out: how many routes exit from an airport
        self.degree_in = [sum(A[:, i]) for i in range(self.n_airports)]     #degree in: how many routes enter in an airport

        self.strength_out = [sum(W[i, :]) for i in range(self.n_airports)]  #strength out: how many total flights exit from an airport: more is high, more is reasonable that more infected people can exit from an airport at time t
        self.strength_in = [sum(W[:, i]) for i in range(self.n_airports)]   #strength in: how many total flights exit from an airport: more is high, more is reasonable that more infected people can arrive in an airport at time t

        self.gamma = gamma
        self.theta = theta
        self.alpha = alpha

        self.n_people_per_airport = [np.sum(A[:, i]) * 100 for i in range(self.n_airports)]                                         #constant value: number of arriving routes*100
        self.infected_per_airport = np.clip(initial_conditions_infected, np.zeros(self.n_airports), self.n_people_per_airport)      #the infected people per airport: intialized with the initial conditions
        self.non_infected_per_airport = self.n_people_per_airport - self.infected_per_airport                                       #the non-infected people per airport: constraint that the sum of this with the number of infected people is equal to the number of total people in the airport


    def probability_new_infected_per_airport(self):

        '''
        Rule for estimating the probability that a non-sick people in the airport gets infected in a time step.
        Now: deterministic function that is directly proportional to the proportion of infected people in the airport
        :return: a list with the probability of a single infection in each airport
        '''
        alpha = 0.25

        a = self.infected_per_airport
        b = self.n_people_per_airport
        infected_ratio = np.divide(a, b, np.zeros(a.shape, dtype=float), where=(b != 0))  # For some reason it still divides by 0.

        # Filter NaN values
        x = []
        for i in range(self.n_airports):
            if math.isnan(infected_ratio[i]):
                x.append(0)
            else:
                x.append(alpha * infected_ratio[i])

        return x
        # return [alpha * (i / j) for i in self.infected_per_airport for j in self.n_people_per_airport]


    def new_infected_per_airport(self):

        '''
        How many new infected in each airport at each time step: binomial rv sample, with the parameters of the binomial as described in yhe constructor
        :return: a np.array containing the number of new infected people in each airport
        '''

        prob_inf = self.probability_new_infected_per_airport()
        probability_list = [binom.rvs(int(self.non_infected_per_airport[i]), prob_inf[i]) for i in range(self.n_airports)]
        return np.array(probability_list, dtype=np.int64)


    def update_infected_per_airport(self, new_infected: np.ndarray[float]):

        '''
        Updating the number of infected and non-infected people per airport
        '''
        self.infected_per_airport += new_infected
        self.non_infected_per_airport -= new_infected

        #return None


    def beta_computation(self):

        '''
        Evaluation of term beta for each airport: it is defined as convex linear combination of the strength of the airport and its influence in the spread of the infection,
        giving more weight to the latter one.
        :return: list with beta_i star, that is beta_i normalized
        '''

        # new infected
        new_infected = self.new_infected_per_airport()
        # update of infected people
        self.update_infected_per_airport(new_infected)

        # evaluaton of beta for each airport and its normalization
        beta_i = [self.alpha * self.strength_in[i] + (1 - self.alpha) * new_infected[i] for i in range(self.n_airports)]
        sum_beta = sum(beta_i)
        beta_star = beta_i / sum_beta

        return beta_star


    def B_computation(self, beta_star):

        '''
        Computation of matrix B: the column i-th is such that every element is equal to beta_star_i
        :return: matrix as np.array
        '''

        B = np.zeros((self.n_airports, self.n_airports))

        for i in range(self.n_airports):
            for j in range(self.n_airports):
                B[i, j] = beta_star[i]

        return B


    def M_computation(self, beta_star: np.ndarray[float]):

        '''
        M evaluated as the paper
        :return: matrix M as np.array
        '''

        M = np.zeros((self.n_airports, self.n_airports))

        # Slow :)
        for i in range(self.n_airports):
            for j in range(self.n_airports):

                if self.degree_out[j] != 0:
                    M[i, j] = self.theta * self.W[j, i] / self.strength_out[j] + (1 - self.theta) * self.A[j, i] / self.degree_out[j]
                else:
                    M[i, j] = beta_star[i]

        return M


    def M_star_computation(self):

        '''
        M_star evaluated as the paper
        :return: M_star matrix as np.array
        '''

        beta_star = self.beta_computation()
        return self.gamma * self.M_computation(beta_star) + (1 - self.gamma) * self.B_computation(beta_star)


    def step(self):

        '''
        The step of the power iteration for reaching the final ranking.
        Matrix-vector product between M_star and the old ranks is computed after the infection happens, and so M_star is updated accordingly
        '''

        M_star = self.M_star_computation()
        self.ranks = M_star.dot(self.ranks)


    def converge(self, tolerance: float, max_iterations: int):

        '''
        Power iteration for reaching the rankings as invariant. The infection happens during the step.
        :param tolerance: difference in the Euclidean norm between two consecutive iterations such that we can consider the convergence reached
        :param max_iterations: max number of iterations after that we stop the algorithm
        :return: the ranks after power iteration is computed
        '''
        for iteration in range(max_iterations):

            # iterations of WPR: power iteration
            prev_ranks = self.ranks
            #here infection happens
            self.step()

            # Return early if we converged enough.
            diff = np.linalg.norm(self.ranks - prev_ranks)

            print("Step {iteration} converged by {diff}".format(iteration=iteration, diff=diff))

            if (diff < tolerance):
                return self.ranks

        return self.ranks
