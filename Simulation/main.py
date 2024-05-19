import pandas as pd
import csv
import graph
import passenger
import airport
import degree_calculate

PASSENGERS_NUM_CO = 10
SIMULATE_TIMESTEP = 30

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

results = []

for i in range(SIMULATE_TIMESTEP):
    # p.simulate_for_one_step(i, g, airports, [])
    # p.simulate_for_one_step(i, g, airports, [3682, 3830, 3364, 1382, 507, 340,
    #                                          3484, 3670, 580, 3797])  # WPR
    # p.simulate_for_one_step(i, g, airports, [3682, 3830, 3364, 340, 3364, 580,
    #                                          507, 1701, 346, 3484])  # WPR for BigAirports with recovery alpha 3
    # p.simulate_for_one_step(i, g, airports,
    #                         [340, 1382, 1701, 580, 3682, 3830, 3364, 3670, 4029, 346])  # PR
    # p.simulate_for_one_step(i, g, airports, [1,
    #                                          50, 2000, 4527, 6472, 8246, 9954, 10234, 10497, 13876])  # Random
    p.simulate_for_one_step(i, g, airports,
                            [340, 1382, 580, 1701, 3682, 3364, 3830, 346, 4029, 3670])  # Degree Centrality

    # p.simulate_for_one_step(i, g, airports,
    #                         [3682, 3830, 3364, 1382, 507, 340, 3484, 3670, 580, 3797, 3406, 3316, 1218, 13696, 3751,
    #                          346, 3930, 2188, 3576, 502, 3077, 3370, 4029, 1555, 1229, 3885, 193, 302, 3395, 478, 1613,
    #                          3876, 345, 3752, 2279, 3998, 3379, 3382, 3393, 2276, 3093, 3494, 3304, 3877, 3462, 1678,
    #                          3550, 3469, 3386, 737, 1824, 3878, 2179, 609, 3374, 3383, 3645, 1638, 2997, 3858, 599, 351,
    #                          3448, 3941, 1386, 3361, 2985, 1230, 3577, 3391, 1524, 11051, 3714, 2564, 3520, 2397, 2948,
    #                          3533, 146, 644, 2072, 3371, 1587, 3376, 3390, 548, 3275, 3375, 1665, 813, 421, 342, 3388,
    #                          1212, 1056, 2359, 156, 3697, 1128, 2709])  # Top 100 shut down
    print(f'STEP: {i}')

    p.show_passengers_infos(airports)
    results.append(p.show_infected_proportion())
    print(airports.status)

# airports.show_current_airports()

# p.show_infected_proportion()
# p.show_positive_passengers()
# print(airports.status)
# p.show_current_location()
print(results)
