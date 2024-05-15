import numpy as np
import pandas as pd
import plotly.express as px
from DEG import DEG


A = pd.read_csv('A.csv', index_col=0)  # Adjacency matrix

#ranking by degree centrality
deg = DEG(A.to_numpy())

#if in or out degree: you have to modify also after in order to save the correct file
ranks = np.array(deg.degree_in)
#ranks = np.array(deg.degree_out)


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

#if in or out degree (first is in degree)
results.to_csv('/Users/andreafranzoni/Documents/Politecnico/Magistrale/V anno/Data Mining/Project/DataMiningProject/RankingResults/DEG_IN/results_deg_in.csv')
#results.to_csv('/Users/andreafranzoni/Documents/Politecnico/Magistrale/V anno/Data Mining/Project/DataMiningProject/RankingResults/DEG_OUT/results_deg_in.csv')


#printing the results
count = 0
for airport_idx in reversed(idx_sort):
    count += 1
    print(count, ": ", "{airport}: {value}".format(airport=airports[airport_idx], value=ranks[airport_idx]))



