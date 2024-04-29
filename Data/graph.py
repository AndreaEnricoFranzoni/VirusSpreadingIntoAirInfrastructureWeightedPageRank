class Graph:
    def __init__(self):
        self.graph = {}
        # self.id2code = {}

    def init_airport(self, airport_id):
        # if airport_id not in self.id2code:
        #     self.id2code[airport_id] = airport_code
        if airport_id not in self.graph:
            self.graph[airport_id] = []

    def add_route(self, airline_id, src_id, dest_id):
        self.graph[src_id].append((airline_id, dest_id))
