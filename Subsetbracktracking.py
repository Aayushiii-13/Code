def find_subsets(arr, n, target):
    dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    for i in range(1, n + 1): 
        for j in range(1, target + 1):
            if arr[i - 1] <= j: #If the current element arr[i-1] can be included
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]] #Exclude or include
            else:
                dp[i][j] = dp[i - 1][j]
    if not dp[n][target]:
        return []
    subsets = []
    def backtrack(i, target, current_subset): # recursive function to construct subsets using the dp table
        if target == 0:
            subsets.append(current_subset[:])
            return
        
        if i == 0: #NO ELEMENTS LEFT
            return
        
        if dp[i - 1][target]: #If the target can be achieved without including the current element (dp[i-1][target] is True), recursively backtrack to the previous element.
            backtrack(i - 1, target, current_subset)
        
        if target >= arr[i - 1] and dp[i - 1][target - arr[i - 1]]:
            current_subset.append(arr[i - 1])
            backtrack(i - 1, target - arr[i - 1], current_subset)
            current_subset.pop()

    backtrack(n, target, [])
    return subsets

arr = [3, 34, 4, 12, 5, 2]
target = 9
n = len(arr)
subsets = find_subsets(arr, n, target)

if subsets:
    print(f"Subsets that sum to {target}:")
    for subset in subsets:
        print(subset)
else:
    print(f"No subsets found that sum to {target}")
