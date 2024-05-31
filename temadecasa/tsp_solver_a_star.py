from queue import PriorityQueue

class TSPSolverAStar:
    def __init__(self, cities, distances):
        self.cities = cities
        self.distances = distances

    def heuristic(self, route):
        # Example heuristic: sum of minimum edge costs to visit remaining cities
        remaining_cities = set(self.cities) - set(route)
        current_city = route[-1]
        return sum(min(self.distances[current_city][city] for city in remaining_cities) for current_city in remaining_cities)

    def solve(self):
        pq = PriorityQueue()
        pq.put((0, [self.cities[0]]))

        best_cost = float('inf')
        best_route = None

        while not pq.empty():
            current_cost, current_route = pq.get()
            current_city = current_route[-1]

            if len(current_route) == len(self.cities):
                current_cost += self.distances[current_city][current_route[0]]
                if current_cost < best_cost:
                    best_cost = current_cost
                    best_route = current_route + [current_route[0]]
                continue

            for next_city in self.cities:
                if next_city not in current_route:
                    new_cost = current_cost + self.distances[current_city][next_city]
                    heuristic_cost = new_cost + self.heuristic(current_route + [next_city])
                    pq.put((heuristic_cost, current_route + [next_city]))

        return best_route, best_cost
