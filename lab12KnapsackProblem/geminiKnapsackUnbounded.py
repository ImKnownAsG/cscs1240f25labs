def unbounded_knapsack_with_trace(W, wt, val, names):
    """
    Solves the Unbounded Knapsack problem and prints the DP array after key updates.
    """
    n = len(val)
    # dp[w] stores the max value for capacity 'w'
    dp = [0] * (W + 1)
    
    print(f"--- Unbounded Knapsack DP Trace (Capacity W={W}) ---")
    
    # Outer loop: Iterate through all capacities 'w' from 1 up to W
    for w in range(1, W + 1):
        
        # Inner loop: Check all items to see which one gives the best result for capacity 'w'
        for i in range(n):
            item_name = names[i]
            item_val = val[i]
            item_wt = wt[i]
            
            # If the item fits into the current capacity 'w'
            if item_wt <= w:
                # Unbounded Recurrence: dp[w] = max(dp[w], item_val + dp[w - item_wt])
                # We look at dp[w - item_wt] (the remaining capacity), which implicitly
                # allows us to choose item 'i' again.
                new_value = item_val + dp[w - item_wt]
                
                if new_value > dp[w]:
                    old_value = dp[w]
                    dp[w] = new_value
                    
                    # Print update trace
                    print(f"Capacity w={w:2}: Updated from {old_value:3} to {new_value:3} by adding Item {item_name} (W={item_wt})")

        # Optional: Print the full DP array after each capacity calculation
        # print(f"\nDP Array after w={w}: {dp}")
        
    print(f"\nFinal DP Array after processing all capacities (0 to {W}):")
    print("Capacity ->", end=" ")
    print(" ".join(f"{c:3}" for c in range(W + 1)))
    print("Max Value ->", end="")
    print(" ".join(f"{v:3}" for v in dp))

    return dp[W]

# Example Usage for Unbounded Knapsack
values = [10, 40, 50]
weights = [1, 3, 4]
names = ["A", "B", "C"]
capacity = 7

max_value_unbounded = unbounded_knapsack_with_trace(capacity, weights, values, names)
print(f"\nFinal Unbounded Knapsack Max Value: {max_value_unbounded}")


def unbounded_knapsack(W, wt, val):
    """
    Solves the Unbounded Knapsack problem using Dynamic Programming.
    :param W: Knapsack capacity (int)
    :param wt: List of item weights (list of int)
    :param val: List of item values (list of int)
    :return: Maximum value that can be put in the knapsack (int)
    """
    n = len(val)
    # dp[w] will store the maximum value achievable with a knapsack capacity 'w'
    dp = [0] * (W + 1)

    # Fill dp[] table in a bottom-up manner
    # Iterate through all possible capacities 'w'
    for w in range(W + 1):
        # For each capacity, check all items
        for i in range(n):
            # If the item can fit into the current capacity 'w'
            if wt[i] <= w:
                # Update dp[w] to the max of:
                # 1. Its current value (not including the item for the last time)
                # 2. Value of item + max value for remaining capacity (w - wt[i]),
                #    which *can* include the same item 'i' again.
                dp[w] = max(dp[w], val[i] + dp[w - wt[i]])

    return dp[W]

# Example Usage
values = [10, 40, 50, 70]
weights = [1, 3, 4, 5]
capacity = 8

max_value_unbounded = unbounded_knapsack(capacity, weights, values)
print(f"Unbounded Knapsack (Max Value): {max_value_unbounded}") # Expected Output: 110
# (Item 4: 70) + (Item 2: 40) = 110. Total weight: 5 + 3 = 8.