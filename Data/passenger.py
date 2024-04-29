import random


class Passenger:
    def __init__(self, graph):
        self.passengers_info = {}
        self.passengers_onboard = {}

    def add_passenger(self, passenger_id, airport_id, infected):
        passenger_info = {"location": airport_id, "infected": infected}
        self.passengers_info[passenger_id] = passenger_info

    def simulate_for_one_step(self, graph):
        self.passengers_onboard.clear()
        for passenger_id, passenger_info in self.passengers_info.items():
            current_location = passenger_info["location"]
            (airline_id, dest_id) = random.choice(graph.graph[current_location])
            if (airline_id, dest_id) not in self.passengers_onboard:
                self.passengers_onboard[(airline_id, dest_id)] = []
            self.passengers_onboard[(airline_id, dest_id)].append(passenger_id)
            # new_location = random.choice(self.graph[str(current_location)])[1]
            # self.passengers_info[passenger_id]["location"] = new_location

        for (airline_id, dest_id), passengers_onboard in self.passengers_onboard.items():
            print((airline_id, dest_id))

    def show_current_location(self):
        for passenger_id, passenger_info in self.passengers_info.items():
            current_location = passenger_info["location"]
            print(f"Passenger ID: {passenger_id}, Current Location: {current_location}")
