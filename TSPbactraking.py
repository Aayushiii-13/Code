import sys

# Function to calculate the minimum cost of a tour using backtracking
def tsp_backtracking(graph, curr_city, visited, count, cost, ans):
    # Base case: if all cities have been visited
    if count == len(graph) - 1:
        # Add the cost to return to the starting city
        if graph[curr_city][0] != 0:
            ans[0] = min(ans[0], cost + graph[curr_city][0])
        return

    # Explore all the unvisited cities
    for city in range(len(graph)):
        if not visited[city] and graph[curr_city][city] != 0:
            visited[city] = True
            tsp_backtracking(graph, city, visited, count + 1, cost + graph[curr_city][city], ans)
            visited[city] = False  # Backtrack

# Wrapper function to start the TSP backtracking process
def solve_tsp(graph):
    n = len(graph)
    visited = [False] * n
    visited[0] = True  # Start from the first city (index 0)
    ans = [sys.maxsize]  # Store the minimum cost found
    tsp_backtracking(graph, 0, visited, 1, 0, ans)
    return ans[0]

# Example input: graph representing distances between cities
graph = [
    [0, 10, 15, 20],  # City 0 to others
    [10, 0, 35, 25],  # City 1 to others
    [15, 35, 0, 30],  # City 2 to others
    [20, 25, 30, 0]   # City 3 to others
]

# Solve the TSP
min_cost = solve_tsp(graph)
print(f"Minimum cost of the tour: {min_cost}")
