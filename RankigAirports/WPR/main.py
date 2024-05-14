import numpy as np
import pandas as pd
from WPR import WPR
from PR import PR

A = pd.read_csv('A.csv', index_col=0)  # Adjacency matrix
W = pd.read_csv('W.csv', index_col=0)  # Weights matrix


initially_infected_at_airports = np.ones(A.shape[0], dtype=float)  # At every airport there is one infected person.
r = WPR(A.to_numpy(), W.to_numpy(), 0.95, 0.9, 0.45, initially_infected_at_airports)
#r = PR(A.to_numpy(),0.95)


# Rank airports.
#WPR
r.converge(1, 25)
ranks = r.ranks

#PR
#r.converge(1,25)
#ranks = pr.ranks


airports = A.keys().tolist()
idx_sort = ranks.argsort()
# idx_sort = range(len(ranks)) # Sorts alphabetically.

for airport_idx in idx_sort:
    print("{airport}: {value}".format(airport=airports[airport_idx], value=ranks[airport_idx]))
