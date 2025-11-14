def knapSack_01_with_trace(W, wt, val, names, n):
    """
    Solves the 0/1 Knapsack problem and prints the DP table after each item.
    """
    # Initialize table K[i][w]
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    print(f"--- 0/1 Knapsack DP Trace (Capacity W={W}) ---")
    
    # Iterate through items (i = 1 to n)
    for i in range(1, n + 1):
        item_name = names[i-1]
        item_val = val[i-1]
        item_wt = wt[i-1]
        
        # Iterate through capacities (w = 0 to W)
        for w in range(W + 1):
            if w == 0:
                K[i][w] = 0
            
            # Case 1: Item fits
            elif item_wt <= w:
                # Max(Exclude: K[i-1][w], Include: item_val + K[i-1][w - item_wt])
                # Note: Uses K[i-1] for the "Include" choice
                K[i][w] = max(item_val + K[i-1][w - item_wt], K[i-1][w])
            
            # Case 2: Item does not fit
            else:
                K[i][w] = K[i-1][w]
        
        # Print the table state after processing item i
        print(f"\n✅ After considering Item {i} ({item_name}, V={item_val}, W={item_wt}):")
        print("Capacity ->", end=" ")
        print(" ".join(f"{c:3}" for c in range(W + 1)))
        
        for r in range(i + 1):
            row_label = f"I{r}" if r > 0 else "Base"
            print(f"{row_label:12}", end="")
            print(" ".join(f"{K[r][c]:3}" for c in range(W + 1)))

    return K[n][W]

# Example Usage for 0/1 Knapsack
values = [6, 10, 12]
weights = [1, 2, 3]
names = ["A", "B", "C"]
capacity = 5
num_items = len(values)

max_value_01 = knapSack_01_with_trace(capacity, weights, values, names, num_items)
print(f"\nFinal 0/1 Knapsack Max Value: {max_value_01}")

def knapSack_01(W, wt, val, n):
    """
    Solves the 0/1 Knapsack problem using Dynamic Programming.
    :param W: Knapsack capacity (int)
    :param wt: List of item weights (list of int)
    :param val: List of item values (list of int)
    :param n: Number of items (int)
    :return: Maximum value that can be put in the knapsack (int)
    """
    # K[i][w] is the max value for capacity w using first i items
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build table K[][] in a bottom-up manner
    for i in range(n + 1):
        for w in range(W + 1):
            # Base case: 0 items or 0 capacity means 0 value
            if i == 0 or w == 0:
                K[i][w] = 0
            
            # If current item's weight is less than or equal to current capacity 'w'
            elif wt[i-1] <= w:
                # Max of (including the item) or (excluding the item)
                # Include: value of item + max value of remaining capacity (w - wt[i-1]) with previous (i-1) items
                # Exclude: max value with previous (i-1) items and same capacity (w)
                K[i][w] = max(val[i-1] + K[i-1][w - wt[i-1]], K[i-1][w])
            
            # If current item's weight is greater than current capacity 'w', exclude it
            else:
                K[i][w] = K[i-1][w]

    return K[n][W]

# Example Usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
num_items = len(values)

max_value_01 = knapSack_01(capacity, weights, values, num_items)
print(f"0/1 Knapsack (Max Value): {max_value_01}") # Expected Output: 220 (100 + 120)