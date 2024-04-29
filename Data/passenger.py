import random


class Passenger:
    def __init__(self, graph):
        self.graph = graph.graph
        self.passengers_info = {}

    def add_passenger(self, passenger_id, airport_id):
        passenger_info = {"location": airport_id}
        self.passengers_info[passenger_id] = passenger_info

    def simulate_for_one_step(self):
        for passenger_id, passenger_info in self.passengers_info.items():
            current_location = passenger_info["location"]
            new_location = random.choice(self.graph[str(current_location)])[1]
            self.passengers_info[passenger_id]["location"] = new_location

    def show_current_location(self):
        for passenger_id, passenger_info in self.passengers_info.items():
            current_location=passenger_info["location"]
            print(f"Passenger ID: {passenger_id}, Current Location: {current_location}")
