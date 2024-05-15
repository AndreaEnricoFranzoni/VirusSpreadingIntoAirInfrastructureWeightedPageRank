import pandas as pd
import csv
import graph
import passenger
import airport
import degree_calculate

PASSENGERS_NUM_CO = 10
SIMULATE_TIMESTEP = 10

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
    if route['Source airport ID'] == '\\N' or route['Destination airport ID'] == '\\N':
        continue
    if int(route['Source airport ID']) in g.graph and int(route['Destination airport ID']) in g.graph:
        g.add_route(int(route['Source airport ID']), int(route['Destination airport ID']))

p = passenger.Passenger(g)

degrees = degree_calculate.get_all_degrees()
for airport_id, _ in airports.airports.items():
    if airport_id not in degrees:
        continue
    passengers_num = PASSENGERS_NUM_CO * degrees[airport_id]
    for _ in range(0, passengers_num):
        passenger_index = p.add_passenger(airport_id, False)
        airports.init_passenger(airport_id, passenger_index)

for passenger_id in airports.airports[737]:
    if passenger_id % 50 == airports.airports[737][0] % 50:
        p.passengers_info[passenger_id]["infected"] = True

for _ in range(SIMULATE_TIMESTEP):
    # p.simulate_for_one_step(g, airports, [3682, 3830, 3364, 1382, 507, 3484, 340, 3670, 3797, 580]) #WPR
    # p.simulate_for_one_step(g, airports, [])
    # p.simulate_for_one_step(g, airports, [340, 1382, 3682, 1701, 580, 3830, 3364, 3670, 4029, 346]) #RPR
    # p.simulate_for_one_step(g, airports, [1, 50, 2000, 4527, 6472, 8246, 9954, 10234, 10497, 13876]) #Random
    # p.simulate_for_one_step(g, airports,
    #                         [340, 1382, 580, 1701, 3682, 3364, 3830, 346, 4029, 3670])  # Degree Centrality-In
    p.simulate_for_one_step(g, airports,
                            [340, 1382, 580, 1701, 3682, 3364, 3830, 346, 4029, 2188])  # Degree Centrality-Out
    p.show_positive_passengers()
    p.show_infected_proportion()

airports.show_current_airports()

p.show_infected_proportion()
# p.show_positive_passengers()
print(airports.status)
# p.show_current_location()