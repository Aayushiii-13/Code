import sys

# Function to solve the TSP using Dynamic Programming (Held-Karp Algorithm)
def tsp_dp(graph):
    n = len(graph)
    # dp[mask][i] represents the minimum cost of visiting cities in 'mask' and ending at city 'i'
    dp = [[sys.maxsize] * n for _ in range(1 << n)]
    
    # Base case: starting from city 0 (initial city)
    dp[1][0] = 0
    
    # Iterate over all possible subsets of cities
    for mask in range(1, 1 << n):
        for u in range(n):
            if (mask & (1 << u)) == 0:
                continue
            # Try to visit every unvisited city 'v'
            for v in range(n):
                if (mask & (1 << v)) == 0:  # If 'v' is not visited
                    new_mask = mask | (1 << v)
                    dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + graph[u][v])
    
    # Find the minimum cost to visit all cities and return to the starting city
    final_mask = (1 << n) - 1  # All cities visited
    min_cost = sys.maxsize
    for i in range(1, n):
        min_cost = min(min_cost, dp[final_mask][i] + graph[i][0])
    
    return min_cost

# Example input: graph representing distances between cities
graph = [
    [0, 10, 15, 20],  # City 0 to others
    [10, 0, 35, 25],  # City 1 to others
    [15, 35, 0, 30],  # City 2 to others
    [20, 25, 30, 0]   # City 3 to others
]

# Solve the TSP
min_cost = tsp_dp(graph)
print(f"Minimum cost of the tour: {min_cost}")
