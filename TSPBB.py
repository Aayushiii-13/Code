import math

def tsp_branch_and_bound(cost_matrix):
    n = len(cost_matrix)
    visited = [False] * n  
    min_cost = float("inf")  # Initialize minimum cost
    best_route = []          # To store the best route

    def bound(node, level, current_cost):
        """Calculate a lower bound for the given node."""
        if level == n - 1:
            return current_cost + cost_matrix[node][0]  # Add cost to return to the start
        min_edges = [
            min(cost_matrix[i][j] for j in range(n) if i != j and not visited[j])
            for i in range(n)
        ]
        return current_cost + sum(min_edges[:n - level])

    def tsp_recursive(node, level, current_cost, path):
        nonlocal min_cost, best_route

        # If all nodes are visited, complete the tour by returning to the start
        if level == n:
            total_cost = current_cost + cost_matrix[node][0]
            if total_cost < min_cost:
                min_cost = total_cost
                best_route = path[:] + [0]
            return

        # Explore paths from the current node to unvisited nodes
        for next_node in range(n):
            if not visited[next_node] and cost_matrix[node][next_node] > 0:
                new_cost = current_cost + cost_matrix[node][next_node]
                if new_cost + bound(next_node, level, new_cost) < min_cost:
                    visited[next_node] = True
                    tsp_recursive(next_node, level + 1, new_cost, path + [next_node])
                    visited[next_node] = False

    visited[0] = True  # Start at the first node
    tsp_recursive(0, 1, 0, [0])  # Start recursive branch and bound

    return min_cost, best_route

# Taking input from the user
n = int(input("Enter the number of cities: "))
print("Enter the cost matrix (enter row by row, space-separated):")
cost_matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    cost_matrix.append(row)

# Solve TSP using Branch and Bound
min_cost, best_route = tsp_branch_and_bound(cost_matrix)
print(f"\nMinimum cost: {min_cost}")
print(f"Optimal route: {best_route}")

# Example Input
# cost_matrix = [
#     [0, 10, 15, 20],
#     [10, 0, 35, 25],
#     [15, 35, 0, 30],
#     [20, 25, 30, 0]
# ]



