def greedy_knapsack_01(weights, values, capacity):
    n = len(weights)

    # Calculate value to weight ratio
    ratios = [(values[i] / weights[i], i) for i in range(n)]
    ratios.sort(reverse=True, key=lambda x: x[0])

    total_value = 0
    total_weight = 0
    selected_items = []

    for ratio, i in ratios:
        # Include the item only if it fits in the knapsack (without exceeding capacity)
        if total_weight + weights[i] <= capacity:
            total_value += values[i]
            total_weight += weights[i]
            selected_items.append(i + 1)  # Adding item index (1-based)

    return total_value, total_weight, selected_items


# Taking input from the user
n = int(input("Enter the number of items: "))
weights = list(map(int, input("Enter weights of items separated by space: ").split()))
values = list(map(int, input("Enter values of items separated by space: ").split()))
capacity = int(input("Enter the capacity of the knapsack: "))

# Solve 0/1 Knapsack using Greedy
total_value, total_weight, selected_items = greedy_knapsack_01(weights, values, capacity)

print(f"\nTotal value: {total_value}")
print(f"Total weight: {total_weight}")
print(f"Selected items: {selected_items}")

# weights = [4, 2, 6, 3, 5]
# values = [12, 1, 10, 7, 6]
# capacity = 20

