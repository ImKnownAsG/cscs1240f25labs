def fractional_knapsack(W, wt, val):
    """
    Solves the Fractional Knapsack problem using a Greedy approach.
    :param W: Knapsack capacity (int or float)
    :param wt: List of item weights (list of int or float)
    :param val: List of item values (list of int or float)
    :return: Maximum value that can be put in the knapsack (float)
    """
    n = len(val)
    # Combine value, weight, and calculate the ratio (value/weight) for each item
    items = []
    for i in range(n):
        ratio = val[i] / wt[i]
        items.append((ratio, val[i], wt[i]))

    # Sort items by ratio in descending order
    items.sort(key=lambda x: x[0], reverse=True)
    
    current_weight = 0
    final_value = 0.0

    for ratio, value, weight in items:
        # If the whole item can fit
        if current_weight + weight <= W:
            current_weight += weight
            final_value += value
        
        # If only a fraction of the item can fit
        else:
            remaining_capacity = W - current_weight
            fraction = remaining_capacity / weight
            final_value += value * fraction
            current_weight = W  # Knapsack is now full
            break
            
    return final_value

# Example Usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value_frac = fractional_knapsack(capacity, weights, values)
print(f"Fractional Knapsack (Max Value): {max_value_frac:.2f}") # Expected Output: 240.00
# Item 1: (60/10=6), Item 2: (100/20=5), Item 3: (120/30=4). Sorted: I1, I2, I3.
# Take all of I1 (10kg, +60), all of I2 (20kg, +100). Remaining capacity: 20kg.
# Take 20/30 of I3: (20/30) * 120 = 80. Total: 60 + 100 + 80 = 240.