import numpy as np
from scipy.stats import binom

class WPR:

    def __init__(self,
                 A,
                 W,
                 gamma: float,
                 theta: float,
                 alpha: float,
                 initial_conditions_infected
                 )->None:

        '''
        Constructor:
        Assumptions: - at each time steps, in each airport, there is a number of people equal to the
                       to the number of arriving fligths*100
                     - number of new infected people: binomial r.v. where n is the number of non-sick people in the airport
                                                      at the beginning of the time step, and p is proportional to the number of infected peopple in the airport

        Algorithm relays on the paper, but since beta changes along the algo, using power iteration

        :param A: adjacency matrix
        :param W: weights matrix
        :param gamma: teleportation parameter ([0,1)): in this case, has to be as high as possible: not dead ends
        :param theta: trade-off degree-weight parameter ([0,1]): in this case, has to be as high as possible: number of flights are more important than number of connections
        :param initial_conditions_infected: number of infected in each airport at time 0
        '''

        if A.shape() != W.shape():
            raise ValueError('A and W need to have the same dimensions')
        if gamma < 0 or gamma >= 1:
            raise ValueError('Gamma has to be in [0,1)')
        if theta < 0 or theta > 1:
            raise ValueError('Theta has to be in [0,1]')
        if alpha < 0 or alpha > 1:
            raise ValueError('Alpha has to be in [0,1]')

        self.A = A
        self.W = W
        self.n_airports = A.shape()[0]
        self.ranks = np.ones(self.n_airports)

        self.degree_out = [sum(A[i,:]) for i in range(self.n_airports)]
        self.degree_in = [sum(A[:,i]) for i in range(self.n_airports)]

        self.strength_out = [sum(W[i,:]) for i in range(self.n_airports)]
        self.strength_in = [sum(W[:,i]) for i in range(self.n_airports)]

        self.gamma = gamma
        self.theta = theta
        self.alpha = alpha

        self.n_people_per_airport = [np.sum(A[i,:]) for i in range(self.n_airports)]*100
        self.infected_per_airport = initial_conditions_infected
        self.non_infected_per_airport = self.n_people_per_airport - self.infected_per_airport


    def probability_new_infected_per_airport(self):

        '''
        Rule for estimating the probability that a non-sick people in the airport
        :return: a list with the probability of a single infection in each airport
        '''
        alpha = 0.25
        return [alpha*(i/j) for i in self.infected_per_airport for j in self.n_people_per_airport]


    def new_infected_per_airport(self,seed):

        '''
        How many new infected in each airport at each time step: binomial rv sample
        :return:
        '''

        prob_inf = self.probability_new_infected_per_airport()
        return [binom(self.non_infected_per_airport[i], prob_inf[i],seed=seed) for i in range(self.n_airports)]


    def update_infected_per_airport(self, new_infected):

        '''
        Updating the number of infected and non-infected people per airport
        '''
        self.infected_per_airport += new_infected
        self.non_infected_per_airport -= new_infected

        return None


    def beta_computation(self,seed):

        '''
        Beta evaluation for each airport: here the infection happens
        :return: list with beta_i
        '''

        #new infected
        new_infected = self.new_infected_per_airport(seed)
        #update of infected people
        self.update_infected_per_airport(new_infected=new_infected)

        #evaluaton of beta for each airport and its normalization
        beta_i = [self.alpha*self.strength_in[i] + (1-self.alpha)*new_infected[i] for i in range(self.n_airports)]
        sum_beta = sum(beta_i)
        beta_star = beta_i/sum_beta

        return beta_star


    def B_computation(self, beta_star):

        '''
        Computation of matrix B as the paper
        :return: matrix B
        '''

        B = np.zeros((self.n_airports,self.n_airports))

        for i in range(self.n_airports):
            for j in range(self.n_airports):

                B[i,j] = beta_star[i]

        return B


    def M_computation(self, beta_star):

        '''
        M evaluated as the paper
        :return: matrix M
        '''

        M = np.zeros((self.n_airports, self.n_airports))

        for i in range(self.n_airports):
            for j in range(self.n_airports):

                if self.degree_out[j] != 0:
                    M[i,j] = self.theta*self.W[j,i]/self.strength_out[j] + (1-self.theta)*self.A[j,i]/self.degree_out[j]
                else:
                     M[i,j] = beta_star[i]


    def M_star_computation(self,beta_star):

        return self.gamma*self.M_computation(beta_star) + (1-self.gamma)*self.B_computation(beta_star)


    def WPR_algo(self,seed):

        tol = 30
        old_ranks = np.array(self.ranks)
        new_ranks = np.array(self.ranks)

        while (tol > 1):
             #iterations of WPR: power iteration
             beta_star = self.beta_computation(seed)
             M_star = self.M_star_computation(beta_star)

             new_ranks = M_star*old_ranks

             tol = np.linalg.norm(new_ranks-old_ranks)
             old_ranks = new_ranks

        self.ranks = new_ranks
 
        return new_ranks





