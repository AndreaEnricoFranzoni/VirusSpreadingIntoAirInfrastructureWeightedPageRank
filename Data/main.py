import numpy as np
import pandas as pd
import csv
import graph
import passenger

PASSENGERS_NUM = 10
SIMULATE_TIMESTEP = 10

g = graph.Graph()

airports_file_path = 'airports.dat'
data_list = []
with open(airports_file_path, 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        data_list.append(row)

dataset = pd.DataFrame(data_list)
dataset.columns = ['Airport ID', 'Name', 'City', 'Country', 'IATA', 'ICAO', 'Latitude', 'Longitude', 'Altitude',
                   'Timezone', 'DST',
                   'Tz database timezone', 'Type', 'Source']

for _, route in dataset.iterrows():
    g.init_airport(route['Airport ID'])

routes_file_path = 'routes.dat'
data_list = []
with open(routes_file_path, 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        data_list.append(row)
dataset = pd.DataFrame(data_list)
dataset.columns = ['Airline', 'Airline ID', 'Source airport', 'Source airport ID', 'Destination airport',
                   'Destination airport ID', 'Codeshare', 'Stops', 'Equipment']

for _, route in dataset.iterrows():
    if route['Source airport ID'] in g.graph and route['Destination airport ID'] in g.graph:
        g.add_route(route['Airline ID'],route['Source airport ID'], route['Destination airport ID'])

p = passenger.Passenger(g)

for index in range(PASSENGERS_NUM):
    p.add_passenger(index, 737)
for _ in range(SIMULATE_TIMESTEP):
    p.simulate_for_one_step()
p.show_current_location()







