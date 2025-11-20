# Python program to find the shortest possible route
# that visits every city exactly once and returns to
# the starting point using memoization and bitmasking

import sys
def totalCost(mask, pos, n, cost):
    # Base case: if all cities are visited, return the
    # cost to return to the starting city (0)
    if mask == (1 << n) - 1:
        print(cost[pos][0])
        return cost[pos][0]

    ans = sys.maxsize
    path = []

    # Try visiting every city that has not been visited yet
    for i in range(n):
        if (mask & (1 << i)) == 0: 
            print(f'pos, i, cost[pos][i], mask: {pos}, {i}, {cost[pos][i]}, {mask:b}')
  
            # If city i is not visited, visit it and 
             #  update the mask
            ans = min(ans, cost[pos][i] +
                      totalCost(mask | (1 << i), i, n, cost))

    return ans
 

def tsp(cost):
    n = len(cost)
    
    # Start from city 0, and only city 0 is visited 
    # initially (mask = 1)
    return totalCost(1, 0, n, cost)
 
if __name__ == "__main__":
    
    cost = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    result = tsp(cost)
    print(f'result: {result}')