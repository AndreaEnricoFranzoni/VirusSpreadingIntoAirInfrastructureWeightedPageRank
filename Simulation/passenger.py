import random
import airport

# Assuming the possibility to be infected on the plane is directly proportional to the number of virus carriers
ALPHA = 0.1

shutdown_threshold = 0.05


class Passenger:
    def __init__(self, graph):
        self.passengers_info = {}

    def add_passenger(self, passenger_id, airport_id, infected):
        passenger_info = {'location': airport_id, 'infected': infected}
        self.passengers_info[passenger_id] = passenger_info

    def simulate_for_one_step(self, graph, airports, impt_airports = []):

        # Whether to shut down

        for airport_id, passengers in airports.airports.items():
            if airport_id in impt_airports:
                infected_ratio = self.calculate_infected_passengers(passengers) / len(passengers)
                if infected_ratio > shutdown_threshold:
                    airports.status[airport_id] = False

        # Transmission
        for passenger_id, passenger_info in self.passengers_info.items():
            current_location = passenger_info['location']
            if not graph.graph[current_location]:  # dead-end
                continue

            if not airports.status[current_location]:
                continue

            proportion = []
            dest_option = []
            for dest_id, route_weight in graph.graph[current_location].items():
                if airports.status[dest_id]:
                    proportion.append(route_weight)
                    dest_option.append(dest_id)
            if len(dest_option) == 0:
                continue
            dest_id = random.choices(dest_option, weights=proportion)[0]
            airports.update_passenger(passenger_id, current_location, dest_id)
            self.passengers_info[passenger_id]['location'] = dest_id

        # Simulate the infection at the airport
        for airport_id, passengers in airports.airports.items():
            if not airports.status[airport_id]:
                continue
            if len(passengers) == 0:
                continue
            infected_num = self.calculate_infected_passengers(passengers)
            infection_possibility = ALPHA * infected_num / len(passengers)
            self.simulate_infection(passengers, infection_possibility)

    def calculate_infected_passengers(self, passengers):
        counter = 0
        for passenger_id in passengers:
            if self.passengers_info[passenger_id]['infected']:
                counter += 1
        return counter

    def simulate_infection(self, passengers, infection_possibility):
        for passenger_id in passengers:
            if not self.passengers_info[passenger_id]['infected']:
                if random.random() < infection_possibility:
                    self.passengers_info[passenger_id]['infected'] = True

    def show_current_location(self):
        for passenger_id, passenger_info in self.passengers_info.items():
            current_location = passenger_info['location']
            print(f'Passenger ID: {passenger_id}, Current Location: {current_location}')

    def show_infected_proportion(self):
        counter = 0
        for passenger_id, passenger_info in self.passengers_info.items():
            if passenger_info['infected']:
                counter += 1
        print(f'Infected Passengers Proportion: {counter / len(self.passengers_info)}')
