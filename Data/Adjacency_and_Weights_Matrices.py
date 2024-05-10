import pandas as pd
import numpy as np
import csv

#reading dataset about routes
routes_file_path = 'routes.dat'
data_list = []
with open(routes_file_path, 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        data_list.append(row)

routes = pd.DataFrame(data_list)
routes.columns = ['Company', 'Airline ID', 'Source airport', 'Source airport ID', 'Destination airport', 'Destinaton airport ID', 'Codeshare', 'Stops', 'Equipment']

#flights
flights = routes[['Source airport','Destination airport']]


#total airports
routes_source = routes['Source airport']
routes_destination = routes['Destination airport']
airport_source = pd.unique(routes_source)
airport_destination = pd.unique(routes_destination)
#there are some airports that are only destinations and others that are only as sources (quite strange by the way)
total_airports = list(map(lambda x: x,set(airport_source).union(set(airport_destination))))
total_airports.sort()
n = len(total_airports)

#creating the the two matrices: A is adjacency, W is weight matrix
#treated as pandas df. Airports are report in alfhabetical ordere
A = pd.DataFrame(np.zeros((n,n), dtype=int),columns=total_airports,index=total_airports)
W = pd.DataFrame(np.zeros((n,n), dtype=int),columns=total_airports,index=total_airports)

#filling them
for index,row in flights.iterrows():

    A.loc[row['Source airport']][row['Destination airport']] = 1
    W.loc[row['Source airport']][row['Destination airport']] += 1

#matrices read and saved in a file to be used in the other scripts
A.to_csv("/Users/andreafranzoni/Documents/Politecnico/Magistrale/V anno/Data Mining/Project/DataMiningProject/Data/A.csv")
W.to_csv("/Users/andreafranzoni/Documents/Politecnico/Magistrale/V anno/Data Mining/Project/DataMiningProject/Data/W.csv")







