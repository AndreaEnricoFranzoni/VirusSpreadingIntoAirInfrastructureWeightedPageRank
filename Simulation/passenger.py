import random
import airport

# Assuming the possibility to be infected on the plane is directly proportional to the number of virus carriers
ALPHA = 0.1
BETA = 10

SHUTDOWN_THRESHOLD = 0.05
SUCCESS_RATE = 0.8


class Passenger:
    def __init__(self, graph):
        self.passengers_info = {}
        self.id_counter = -1

    def add_passenger(self, airport_id, infected):
        self.id_counter += 1
        passenger_info = {'location': airport_id, 'infected': infected, 'test_positive': False, 'infected_time': -1}
        self.passengers_info[self.id_counter] = passenger_info
        return self.id_counter

    def simulate_for_one_step(self, timestamp, graph, airports, impt_airports=[]):

        # Whether to shut down

        for airport_id, passengers in airports.airports.items():
            if len(passengers) == 0:
                continue
            if airport_id in impt_airports:
                for passenger_id in passengers:
                    if self.passengers_info[passenger_id]['infected']:
                        if random.random() < SUCCESS_RATE:
                            self.passengers_info[passenger_id]['test_positive'] = True

                positive_ratio = self.calculate_positive_passengers(passengers) / len(passengers)
                if positive_ratio > SHUTDOWN_THRESHOLD:
                    airports.status[airport_id] = False

        # Transmission
        for passenger_id, passenger_info in self.passengers_info.items():

            if passenger_info['infected_time'] != -1:
                if timestamp - passenger_info['infected_time'] == 5:
                    passenger_info['infected'] = False
                    passenger_info['infected_time'] = -1
                    passenger_info['test_positive'] = False

            if passenger_info['test_positive']:
                continue

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
            undetected_num = self.calculate_undetected_passengers(passengers)
            infection_possibility = BETA * ALPHA * undetected_num / (
                    len(passengers) - self.calculate_positive_passengers(passengers))
            self.simulate_infection(timestamp, passengers, min(infection_possibility, ALPHA))

    def calculate_undetected_passengers(self, passengers):
        counter = 0
        for passenger_id in passengers:
            if self.passengers_info[passenger_id]['infected'] and not self.passengers_info[passenger_id][
                'test_positive']:
                counter += 1
        return counter

    def calculate_positive_passengers(self, passengers):
        counter = 0
        for passenger_id in passengers:
            if self.passengers_info[passenger_id]['test_positive']:
                counter += 1
        return counter

    def simulate_infection(self, timestamp, passengers, infection_possibility):
        for passenger_id in passengers:
            if not self.passengers_info[passenger_id]['infected']:
                if random.random() < infection_possibility:
                    self.passengers_info[passenger_id]['infected'] = True
                    self.passengers_info[passenger_id]['infected_time'] = timestamp

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
        return counter / len(self.passengers_info)

    def show_positive_passengers(self):
        for passenger_id, passenger_info in self.passengers_info.items():
            if passenger_info['test_positive']:
                print(f'Positive Passenger: {passenger_id}')

    def show_passengers_infos(self, airports):
        for airport_id, passengers in airports.airports.items():
            print('------------------------------------')
            print(f'Airport: {airport_id}')
            for passenger_id in passengers:
                infected = self.passengers_info[passenger_id]['infected']
                print(f'P: {passenger_id}, I: {infected} ', end='')
            print(' ')
