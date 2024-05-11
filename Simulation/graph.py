class Graph:
    def __init__(self):
        self.graph = {}

    def init_airport(self, airport_id):
        if airport_id not in self.graph:
            self.graph[airport_id] = {}

    def add_route(self, src_id, dest_id):
        if dest_id not in self.graph[src_id]:
            self.graph[src_id][dest_id] = 1
        else:
            self.graph[src_id][dest_id] += 1
