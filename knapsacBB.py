import math

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def knapsack_bb(weights, values, W, n):
    items = [Item(values[i], weights[i]) for i in range(n)]
    items.sort(key=lambda x: x.ratio, reverse=True)  
    def bound(i, current_weight, current_value):
        if current_weight >= W:
            return 0  
        profit_bound = current_value
        total_weight = current_weight

        while i < n and total_weight + items[i].weight <= W:
            total_weight += items[i].weight
            profit_bound += items[i].value
            i += 1

        if i < n:
            profit_bound += (W - total_weight) * items[i].ratio  

        return profit_bound

    def branch_and_bound():
        max_profit = 0
        queue = []
        queue.append((-1, 0, 0)) 
        while queue:
            level, current_weight, current_value = queue.pop()

            if level == n - 1:
                continue

            if current_weight + weights[level + 1] <= W:
                new_weight = current_weight + weights[level + 1]
                new_value = current_value + values[level + 1]
                if new_value > max_profit:
                    max_profit = new_value
                queue.append((level + 1, new_weight, new_value))

            if bound(level + 1, current_weight, current_value) > max_profit:
                queue.append((level + 1, current_weight, current_value))

        return max_profit

    return branch_and_bound()

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
W = 5
n = len(weights)
print(f"Maximum value (Branch and Bound): {knapsack_bb(weights, values, W, n)}")
