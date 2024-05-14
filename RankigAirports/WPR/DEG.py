import numpy as np
import math
from scipy.stats import binom


class DEG:
    """ Degree centrality. """

    def __init__(self,
                 A,
                 ) -> None:

        self.A = A
        self.n_airports = A.shape[0]                                        #how many airports

        self.degree_out = [sum(A[i, :]) for i in range(self.n_airports)]    # degree out: how many routes exit from an airport
        self.degree_in = [sum(A[:, i]) for i in range(self.n_airports)]     # degree in: how many routes enter in an airport
