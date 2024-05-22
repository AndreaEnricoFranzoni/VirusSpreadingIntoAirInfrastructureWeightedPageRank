import numpy as np
import pandas as pd


def BFS(A, element):

    n = A.shape[0]
    distances = np.zeros(n,dtype=int)
    distances_old = np.zeros(n, dtype=int)

    k = 1

    for i in range(n):
        if (A[element, i] == 1):
            distances[i] = k

    while (np.linalg.norm(distances - distances_old) > 0.0):

        k += 1
        distances_old = distances

        for i in range(n):
            if (distances[i] == (k - 1)):
                for j in range(n):
                    if (A[i, j] == 1 and distances[j] == 0 and j!=element):
                        distances[j] = k

    return distances