import itertools
import sys

# --- 1. Naive Brute-Force Approach ---
# (No changes to this section)

def solve_tsp_naive(cost_matrix):
    """
    Solves TSP using a naive brute-force approach.
    Checks all n! permutations of cities.
    """
    n = len(cost_matrix)
    cities_to_visit = list(range(1, n))
    min_cost = float('inf')
    best_path = []

    # Iterate through all permutations of the cities to visit
    for path_permutation in itertools.permutations(cities_to_visit):
        current_path = [0] + list(path_permutation) + [0]  # Complete cycle: 0 -> ... -> 0
        current_cost = 0
        
        # Calculate the cost of the current path
        for i in range(n):
            current_cost += cost_matrix[current_path[i]][current_path[i+1]]
        
        if current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path
            
    return min_cost, best_path

# --- 2. Dynamic Programming Approach (Held-Karp Algorithm) ---
# FIX: Complete overhaul of the final mask and path reconstruction for reliability.

def solve_tsp_dp(cost_matrix):
    """
    Solves TSP using the Held-Karp dynamic programming algorithm.
    Time Complexity: O(n^2 * 2^n)
    """
    n = len(cost_matrix)
    
    # Memoization table: memo[(mask, j)] stores min cost to visit cities in 'mask', ending at 'j'.
    # Mask is represented by bits 0 to n-1. Bit 0 is always set (city 0 is start).
    memo = {}
    
    # Path reconstruction table: parent[(mask, j)] stores the predecessor city 'k'.
    parent = {}

    # Base case: Cost from 0 to j (mask = {0, j})
    for j in range(1, n):
        # Mask: bit 0 set (start), bit j set (end) -> (1 << 0) | (1 << j)
        mask = 1 | (1 << j)
        memo[(mask, j)] = cost_matrix[0][j]
        parent[(mask, j)] = 0 # Predecessor of j is 0

    # Main DP loop: Iterate through all subsets of size 3 up to n (r = number of cities in subset)
    for r in range(3, n + 1):
        # Iterate through all masks where 'r' bits are set
        for mask in range(1, 1 << n):
            if bin(mask).count('1') != r or not (mask & 1): # Must have 'r' cities and include city 0
                continue

            # 'j' is the city that is the last one visited in the current subset (mask)
            for j in range(1, n):
                if (mask & (1 << j)): # Check if city j is in the current subset/mask
                    prev_mask = mask ^ (1 << j) # Remove city j from the mask
                    min_prev_cost = float('inf')
                    best_prev_city = -1
                    
                    # 'k' is the city visited just before city j (k must be in prev_mask)
                    for k in range(n):
                        if k != j and (prev_mask & (1 << k)):
                            # Cost = Cost to reach 'k' in 'prev_mask' + Cost from 'k' to 'j'
                            cost_to_k = memo.get((prev_mask, k), float('inf'))
                            current_cost = cost_to_k + cost_matrix[k][j]
                            
                            if current_cost < min_prev_cost:
                                min_prev_cost = current_cost
                                best_prev_city = k
                    
                    if best_prev_city != -1:
                        memo[(mask, j)] = min_prev_cost
                        parent[(mask, j)] = best_prev_city

    # Final step: Calculate the cost to return to city 0
    final_mask = (1 << n) - 1 # All cities visited mask (bits 0 to n-1 set)
    min_cost = float('inf')
    last_city_on_path = -1 # The city just before city 0 on the optimal path

    for j in range(1, n):
        # Total cost = Min cost to reach j in final_mask + Cost from j back to 0
        total_cost = memo.get((final_mask, j), float('inf')) + cost_matrix[j][0]
        
        if total_cost < min_cost:
            min_cost = total_cost
            last_city_on_path = j
            
    # Path Reconstruction
    path = []
    if last_city_on_path != -1:
        # 1. Add the start and end points (city 0)
        path.append(0)
        path.append(last_city_on_path)
        
        current_mask = final_mask
        current_city = last_city_on_path
        
        # 2. Backtrack using the parent dictionary
        while True:
            # Get the predecessor city 'k'
            prev_city = parent.get((current_mask, current_city))
            
            if prev_city == 0:
                # We have reached the start city, stop backtracking.
                break
            
            # Add the predecessor city to the path
            path.append(prev_city)
            
            # Update the mask and current city for the next iteration
            current_mask = current_mask ^ (1 << current_city) # Remove current_city from the mask
            current_city = prev_city
        
        # The path is currently 0 -> last_city -> ... -> 1st_city -> 0 (in reverse order)
        # We need to reverse the intermediate segment and append the final 0.
        path_segment = path[1:] # Segment is [last_city, prev_city, ..., 1st_city]
        path_segment.reverse() 
        path = [0] + path_segment + [0]

    return min_cost, path

# --- 3. Backtracking Approach (with implicit pruning) ---
# (No changes to this section)

def solve_tsp_backtracking(cost_matrix):
    """
    Solves TSP using a recursive backtracking (Depth First Search) approach.
    """
    n = len(cost_matrix)
    min_cost = float('inf')
    best_path = []

    def tsp_recursive(current_cost, current_path, visited_mask):
        nonlocal min_cost, best_path
        
        # Base case: All cities have been visited
        if visited_mask == (1 << n) - 1:
            last_city = current_path[-1]
            total_cost = current_cost + cost_matrix[last_city][0]
            
            if total_cost < min_cost:
                min_cost = total_cost
                best_path = current_path + [0] 
            return

        # Pruning: If current cost is already greater than min_cost, stop
        if current_cost >= min_cost:
            return

        # Recursive step: Try to move to any unvisited city
        last_city = current_path[-1]
        for next_city in range(n):
            if not (visited_mask & (1 << next_city)):
                new_visited_mask = visited_mask | (1 << next_city)
                new_path = current_path + [next_city]
                new_cost = current_cost + cost_matrix[last_city][next_city]
                
                tsp_recursive(new_cost, new_path, new_visited_mask)

    # Start the search from city 0.
    tsp_recursive(0, [0], 1)
    
    return min_cost, best_path

# --- Execution and Output ---

# 1. Naive Approach Cost Matrix (4 cities)
cost_naive = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
min_cost_naive, path_naive = solve_tsp_naive(cost_naive)

# 2. Dynamic Programming Cost Matrix (5 cities)
cost_dp = [
    [0, 2, 4, 7, 1],
    [2, 0, 3, 5, 8],
    [4, 3, 0, 6, 2],
    [7, 5, 6, 0, 9],
    [1, 8, 2, 9, 0]
]
min_cost_dp, path_dp = solve_tsp_dp(cost_dp)

# 3. Backtracking Cost Matrix (4 cities)
cost_backtrack = [
    [0, 1, 10, 1],
    [1, 0, 1, 10],
    [10, 1, 0, 1],
    [1, 10, 1, 0]
]
min_cost_backtrack, path_backtrack = solve_tsp_backtracking(cost_backtrack)

print("## 🗺️ Traveling Salesman Problem Solutions\n")
print("---")
print("### 1. Naive Brute-Force Approach (4 Cities)")
print(f"Cost Matrix (4x4):\n")
for _ in cost_naive:
    print(_)
print(f"Minimum Cost: {min_cost_naive}")
print(f"Optimal Path: {path_naive}")
print("---")
print("### 2. Dynamic Programming Approach (Held-Karp) (5 Cities)")
print(f"Cost Matrix (5x5):\n")
for _ in cost_dp:
    print(_)
print(f"Minimum Cost: {min_cost_dp}")
print(f"Optimal Path: {path_dp}")
print("---")
print("### 3. Backtracking (Recursive DFS) Approach (4 Cities)")
print(f"Cost Matrix (4x4):\n")
for _ in cost_backtrack:
    print(_)
print(f"Minimum Cost: {min_cost_backtrack}")
print(f"Optimal Path: {path_backtrack}")
print("---")