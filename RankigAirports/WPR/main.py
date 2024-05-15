import numpy as np
import pandas as pd
import plotly.express as px
from WPR import WPR


A = pd.read_csv('A.csv', index_col=0)  # Adjacency matrix
W = pd.read_csv('W.csv', index_col=0)  # Weights matrix

gamma = 0.95    #teleportation parameter
theta = 0.9     #tradeoff between strenght and degree: more is high, more importance we are giving to number of flights wrt number of connections: more reasonable
alpha = 0.45    #tradeoff between strength and infection


#initial conditions

#FIRST CASE
#only 2% of people in Stockholm ARL is infected
name_airports_with_infected = ["FRA", "CDG", "AMS", "IST", "ATL", "PEK", "ORD", "MUC", "DME", "DXB"]

#SECOND CASE
#name_airports_with_infected = ("FRA", "CDG")



initially_infected_at_airports = np.zeros(A.shape[0], dtype=float)


people_at_airport = [np.sum(A.to_numpy()[:, i]) * 100 for i in range(A.to_numpy().shape[0])]

for airport_code in name_airports_with_infected:
    index = A.keys().tolist().index(airport_code)
    total_people_at_this_airport = people_at_airport[index]
    initially_infected_at_airports[index] = 0.02 * total_people_at_this_airport



#probability that one people get infected: alpha*proportion of infected people in the airport
# p_alpha = 0.1
#p_alpha = 0.25
# p_alpha = 0.5

p_alphas = [0.1, 0.25, 0.5]

for p_alpha in p_alphas:
    wpr = WPR(A.to_numpy(), W.to_numpy(), gamma=gamma, theta=theta, alpha=alpha, p_alpha=p_alpha, initial_conditions_infected=initially_infected_at_airports)


    tol = 5e-1
    max_iter = 100
    wpr.converge(tolerance=tol, max_iterations=max_iter)

    ranks = wpr.ranks



    airports_data = pd.read_csv('airports.csv')
    airports = A.keys().tolist()
    idx_sort = ranks.argsort()



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

    results.to_csv(f"/Users/lscheibel/Projects/DataMiningProject/RankingResults/WPR/without_recovery/BigAirports/results_WPR_big_airports_{p_alpha}.csv")

    #printing the results
    count = 0
    for airport_idx in reversed(idx_sort):
        count += 1
        print(count, ": ", "{airport}: {value}".format(airport=airports[airport_idx], value=ranks[airport_idx]))





