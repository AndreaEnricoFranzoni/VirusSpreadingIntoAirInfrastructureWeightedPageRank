import random

# Assuming the possibility to be infected on the plane is directly proportional to the number of virus carriers
ALPHA = 0.1


class Passenger:
    def __init__(self, graph):
        self.passengers_info = {}
        self.passengers_onboard = {}

    def add_passenger(self, passenger_id, airport_id, infected):
        passenger_info = {'location': airport_id, 'infected': infected}
        self.passengers_info[passenger_id] = passenger_info

    def simulate_for_one_step(self, graph):
        # Countering boarding passengers
        self.passengers_onboard.clear()
        for passenger_id, passenger_info in self.passengers_info.items():
            current_location = passenger_info['location']
            if len(graph.graph[current_location]) == 0:
                continue

            (airline_id, dest_id) = random.choice(graph.graph[current_location])
            if (airline_id, dest_id) not in self.passengers_onboard:
                self.passengers_onboard[(airline_id, dest_id)] = []
            self.passengers_onboard[(airline_id, dest_id)].append(passenger_id)
            # new_location = random.choice(self.graph[str(current_location)])[1]
            # self.passengers_info[passenger_id]["location"] = new_location

        # Simulate the infection on the airplane
        for (airline_id, dest_id), passengers_onboard in self.passengers_onboard.items():
            infected_counter = 0
            for passenger_id in passengers_onboard:
                if self.passengers_info[passenger_id]['infected']:
                    infected_counter += 1
            infected_possibility = ALPHA * infected_counter
            for passenger_id in passengers_onboard:
                if not self.passengers_info[passenger_id]['infected']:
                    if random.random() < infected_possibility:
                        self.passengers_info[passenger_id]['infected'] = True

        # Update locations
        for (airline_id, dest_id), passengers_onboard in self.passengers_onboard.items():
            for passenger_id in passengers_onboard:
                self.passengers_info[passenger_id]['location'] = dest_id

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
