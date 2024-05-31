from tsp_solver_dfs import TSPSolverDFS
from tsp_solver_ucs import TSPSolverUCS
from tsp_solver_a_star import TSPSolverAStar
import random

def generate_random_tsp(n):
    cities = list(range(n))
    distances = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        distances[i][i] = 0
    return cities, distances

def main():
    cities, distances = generate_random_tsp(5)
    
    dfs_solver = TSPSolverDFS(cities, distances)
    ucs_solver = TSPSolverUCS(cities, distances)
    a_star_solver = TSPSolverAStar(cities, distances)

    dfs_route, dfs_cost = dfs_solver.solve()
    ucs_route, ucs_cost = ucs_solver.solve()
    a_star_route, a_star_cost = a_star_solver.solve()

    print("DFS Route:", dfs_route, "Cost:", dfs_cost)
    print("UCS Route:", ucs_route, "Cost:", ucs_cost)
    print("A* Route:", a_star_route, "Cost:", a_star_cost)

if __name__ == "__main__":
    main()
