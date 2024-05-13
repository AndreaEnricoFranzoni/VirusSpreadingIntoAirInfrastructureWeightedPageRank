import numpy as np
import math


class PR:

    def __init__(self,
                 A,
                 gamma: float
                 ) -> None:

        '''
        Constructor:
        vanilla implementation of the PageRank algorithm

        :param A: adjacency matrix
        :param gamma: teleportation parameter ([0,1)): in this case, has to be as high as possible: not dead ends in the graph (?)
        '''

        if gamma < 0 or gamma >= 1:
            raise ValueError('Gamma has to be in [0,1)')

        self.A = A
        self.n_airports = A.shape[0]                                        #how many airports
        self.ranks = np.ones(self.n_airports)                               #at the beginning, all the airports have the same rank

        self.degree_out = [sum(A[i, :]) for i in range(self.n_airports)]    #degree out: how many routes exit from an airport
        self.degree_in = [sum(A[:, i]) for i in range(self.n_airports)]     #degree in: how many routes enter in an airport

        self.gamma = gamma


    def M_computation(self):

        '''
        M evaluated as the paper
        :return: matrix M as np.array
        '''

        M = np.zeros((self.n_airports, self.n_airports))

        # Slow :)
        for i in range(self.n_airports):
            for j in range(self.n_airports):

                if (self.A[j,i]!=0):
                    




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