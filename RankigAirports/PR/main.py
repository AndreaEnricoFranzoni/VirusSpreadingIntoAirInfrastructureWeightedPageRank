import numpy as np
import pandas as pd
import plotly.express as px
from PR import PR


A = pd.read_csv('A.csv', index_col=0)  # Adjacency matrix
gamma = 0.95    #teleportation parameter

#tolerance
tol = 1
max_iter = 100

pr = PR(A.to_numpy(), gamma=gamma)
pr.converge(tolerance=tol, max_iterations=max_iter)
ranks = pr.ranks

#order of results
airports_data = pd.read_csv('airports.csv')
airports = A.keys().tolist()
idx_sort = ranks.argsort()
# idx_sort = range(len(ranks)) # Sorts alphabetically.


#saving it as pd dataframe and then as .csv in the appropriate directory
results = pd.DataFrame(columns=['Airport', 'Ranking'])

for airports_idx in reversed(idx_sort):
    new_line = pd.DataFrame({'Airport': [airports[airports_idx]], 'Ranking': [ranks[airports_idx]]})
    results = pd.concat([results, new_line], ignore_index=True)

results.to_csv('/Users/andreafranzoni/Documents/Politecnico/Magistrale/V anno/Data Mining/Project/DataMiningProject/RankingResults/PR/results_PR.csv')


#printing the results
count = 0
for airport_idx in reversed(idx_sort):
    count += 1
    print(count, ": ", "{airport}: {value}".format(airport=airports[airport_idx], value=ranks[airport_idx]))

