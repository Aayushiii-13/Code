def knapsack_dp(weights, values, W, n):
    # Create a DP table with dimensions (n+1) x (W+1)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    # Build the table row by row
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][W]

# Input from the user
n = int(input("Enter the number of items: "))  # Number of items
weights = list(map(int, input(f"Enter the weights of {n} items separated by space: ").split()))
values = list(map(int, input(f"Enter the values of {n} items separated by space: ").split()))
W = int(input("Enter the capacity of the knapsack: "))

# Ensure input is valid
if len(weights) != n or len(values) != n:
    print("Error: Number of weights and values must match the number of items!")
else:
    # Solve the knapsack problem
    max_value = knapsack_dp(weights, values, W, n)
    print(f"Maximum value that can be obtained: {max_value}")

#example
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
W = 5
n = len(weights)
print(f"Maximum value: {knapsack_dp(weights, values, W, n)}")
