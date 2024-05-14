import numpy as np
import pandas as pd
from WPR import WPR
from PR import PR

A = pd.read_csv('A.csv', index_col=0)  # Adjacency matrix
W = pd.read_csv('W.csv', index_col=0)  # Weights matrix




# At every airport there is one infected person.
# Since there is no recovery atm, everybody will be infected after just a few time steps.
initially_infected_at_airports = np.ones(A.shape[0], dtype=float)
# initially_infected_at_airports[A.keys().tolist().index("ARN")] = 1

wpr = WPR(A.to_numpy(), W.to_numpy(), 0.95, 0.9, 0.45, initially_infected_at_airports)



# Rank airports.
#WPR
#wpr.converge(1, 25)
#PR


#ranks_wpr = wpr.ranks


pr = PR(A.to_numpy(),0.95)
pr.converge(1,2)
ranks_pr = pr.ranks
airports = A.keys().tolist()
idx_sort = ranks_pr.argsort()
# idx_sort = range(len(ranks)) # Sorts alphabetically.

for airport_idx in idx_sort:
    print("{airport}: {value}".format(airport=airports[airport_idx], value=ranks_pr[airport_idx]))
