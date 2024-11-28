import sys

def nearest_neighbor(graph):
    n = len(graph)
    visited = [False] * n
    current_city = 0  
    visited[current_city] = True
    total_cost = 0
    visited_cities = [current_city]
    
    for _ in range(n - 1):
        nearest_city = -1
        nearest_distance = sys.maxsize
        for city in range(n):
            if not visited[city] and graph[current_city][city] < nearest_distance:
                nearest_distance = graph[current_city][city]
                nearest_city = city
        visited[nearest_city] = True
        total_cost += nearest_distance
        visited_cities.append(nearest_city)
        current_city = nearest_city

    total_cost += graph[current_city][0]
    
    return total_cost, visited_cities

graph = [
    [0, 10, 15],  
    [10, 0, 35],  
    [15, 35, 0]   
]

cost, path = nearest_neighbor(graph)
print("Estimated cost of the tour (Nearest Neighbor):", cost)
print("Path taken:", path)
