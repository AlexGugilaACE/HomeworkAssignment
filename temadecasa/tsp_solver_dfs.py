class TSPSolverDFS:
    def __init__(self, cities, distances):
        self.cities = cities
        self.distances = distances
        self.best_cost = float('inf')
        self.best_route = None

    def dfs(self, current_city, visited, current_route, current_cost):
        if len(visited) == len(self.cities):
            current_cost += self.distances[current_city][current_route[0]]
            if current_cost < self.best_cost:
                self.best_cost = current_cost
                self.best_route = current_route + [current_route[0]]
            return

        for next_city in self.cities:
            if next_city not in visited:
                self.dfs(next_city, visited | {next_city}, current_route + [next_city], current_cost + self.distances[current_city][next_city])

    def solve(self):
        self.dfs(self.cities[0], {self.cities[0]}, [self.cities[0]], 0)
        return self.best_route, self.best_cost
