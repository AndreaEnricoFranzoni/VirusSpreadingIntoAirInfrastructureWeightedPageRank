class Airport:
    def __init__(self):
        self.airports = {}
        self.status = {}

    def init_airport(self, airport_id):
        if airport_id not in self.airports:
            self.airports[airport_id] = []
            self.status[airport_id] = True

    def init_passenger(self, airport_id, passenger_id):
        self.airports[airport_id].append(passenger_id)

    def update_passenger(self, passenger_id, old_location, new_location):
        self.airports[old_location].remove(passenger_id)
        self.airports[new_location].append(passenger_id)

    def show_current_airports(self):
        for airport_id, passengers in self.airports.items():
            print(f'Airport ID: {airport_id}, Passengers: {passengers}')
