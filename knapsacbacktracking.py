def knapsack_backtrack(weights, values, W, n):
    def knapsack_helper(i, current_weight, current_value):
        # Base case: If all items have been considered, return the current value
        if i == n:
            return current_value

        # Exclude the current item and move to the next one
        max_value = knapsack_helper(i + 1, current_weight, current_value)

        # Include the current item if it fits in the knapsack
        if current_weight + weights[i] <= W:
            max_value = max(max_value, knapsack_helper(i + 1, current_weight + weights[i], current_value + values[i]))

        return max_value

    # Start the recursive function from the first item with weight 0 and value 0
    return knapsack_helper(0, 0, 0)


# Accept user input for weights, values, and knapsack capacity
n = int(input("Enter the number of items: "))
weights = []
values = []

for i in range(n):
    weight = int(input(f"Enter weight of item {i+1}: "))
    value = int(input(f"Enter value of item {i+1}: "))
    weights.append(weight)
    values.append(value)

W = int(input("Enter the capacity of the knapsack: "))

# Call the knapsack function and print the result
max_value = knapsack_backtrack(weights, values, W, n)
print(f"The maximum value that can be carried in the knapsack is: {max_value}")



#example
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
W = 5
n = len(weights)
print(f"Maximum value (backtracking): {knapsack_backtrack(weights, values, W, n)}")
