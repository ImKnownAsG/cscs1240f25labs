import permutations

# Python program to find the shortest possible route
# that visits every city exactly once and returns to
# the starting point

def tsp(cost):

    # Number of nodes
    numNodes = len(cost)
    nodes = list(range(numNodes))

    minCost = float('inf')
    
    swapList = permutations.swaps(numNodes)

    # Generate all permutations of the
    # remaining nodes
    for perm in permutations.perm(nodes, swapList):
        currCost = 0
        currNode = 0

        # Calculate the cost of the current permutation
        for node in perm:
            currCost += cost[currNode][node]
            currNode = node

        # Add the cost to return to the starting node
        currCost += cost[currNode][0]

        # Update the minimum cost if the current cost 
        # is lower
        minCost = min(minCost, currCost)

    return minCost


if __name__ == "__main__":

    cost = [
    [0, 1, 10, 1],
    [1, 0, 1, 10],
    [10, 1, 0, 1],
    [1, 10, 1, 0]
]

    res = tsp(cost)
    print(res)
    
'''    
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
print("---")'''