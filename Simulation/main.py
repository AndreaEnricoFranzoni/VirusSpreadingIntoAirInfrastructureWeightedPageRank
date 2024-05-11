import pandas as pd
import csv
import graph
import passenger
import airport

PASSENGERS_NUM = 100000
SIMULATE_TIMESTEP = 1

g = graph.Graph()
airports = airport.Airport()

airports_file_path = '../Data/airports.dat'
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
    g.init_airport(int(route['Airport ID']))
    airports.init_airport(int(route['Airport ID']))

routes_file_path = '../Data/routes.dat'
data_list = []
with open(routes_file_path, 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        data_list.append(row)
dataset = pd.DataFrame(data_list)
dataset.columns = ['Airline', 'Airline ID', 'Source airport', 'Source airport ID', 'Destination airport',
                   'Destination airport ID', 'Codeshare', 'Stops', 'Equipment']

for _, route in dataset.iterrows():
    if route['Source airport ID'] == "\\N" or route['Destination airport ID'] == '\\N':
        continue
    if int(route['Source airport ID']) in g.graph and int(route['Destination airport ID']) in g.graph:
        g.add_route(int(route['Source airport ID']), int(route['Destination airport ID']))

p = passenger.Passenger(g)

for index in range(PASSENGERS_NUM):
    if index == 0:
        p.add_passenger(index, 737, True)

    else:
        p.add_passenger(index, 737, False)

    airports.init_passenger(737, index)



for _ in range(SIMULATE_TIMESTEP):
    p.simulate_for_one_step(g, airports)

airports.show_current_airports()

p.show_infected_proportion()
# p.show_current_location()
