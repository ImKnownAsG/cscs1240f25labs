# Function to add an edge to an undirected graph
def add_edge(adj_matrix, i, j):
    adj_matrix[i][j] = 1
    adj_matrix[j][i] = 1

# Function to display the adjacency matrix
def display_matrix(mat):
    print("Adjacency Matrix:")
    for row in mat:
        print(row)
        print(" ".join(map(str, row)))
    
    for col in mat:
        print(col)
        print(" ".join(map(str, col)))

# Function to create an adjacency list from a matrix
def create_adj_list(adj_matrix):
    adj_list = [[] for _ in range(len(adj_matrix))]
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix)):
            if adj_matrix[i][j] == 1:
                adj_list[i].append(j)
    return adj_list

# Function to display the adjacency list
def display_list(adj_list):
    print("\nAdjacency List:")
    for i, neighbors in enumerate(adj_list):
        print(f"{i}: {neighbors}")

# Depth First Search traversal using the adjacency matrix
def dfs_traversal_matrix(adj_matrix, start_node):
    print(f"\nDepth First Traversal (using matrix, starting from node {start_node}):")
    startTime = int(round(time.time() * 1000000))
    print(f"Starting at: {startTime}")    
    V = len(adj_matrix)
    visited = [False] * V
    stack = [start_node]
    visited[start_node] = True
    traversal_path = []

    while stack:
        current_node = stack.pop()
        traversal_path.append(current_node)

        # Iterate through the row corresponding to the current node
        # to find its neighbors.
        # We iterate in reverse to ensure the smallest node is explored first
        # due to the LIFO nature of the stack.
        for neighbor in range(V - 1, -1, -1):
            if adj_matrix[current_node][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)

    print(traversal_path)
    endTime = int(round(time.time() * 1000000))
    print(f"Ending at: {endTime}")
    print(f"Elapsed time: {endTime - startTime}")

# Depth First Search traversal
def dfs_traversal(adj_list, start_node):
    print(f"\nDepth First Traversal (starting from node {start_node}):")
    startTime = int(round(time.time() * 1000000))
    print(f"Starting at: {startTime}")
    visited = [False] * len(adj_list)
    stack = [start_node]
    visited[start_node] = True
    traversal_path = []
    while stack:
        current_node = stack.pop()
        traversal_path.append(current_node)

        # Sort neighbors in reverse order to ensure the smallest node is processed first
        # This is because the stack is LIFO (Last-In, First-Out)
        neighbors = sorted(adj_list[current_node], reverse=True)
        for neighbor in neighbors:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
    print(traversal_path)
    endTime = int(round(time.time() * 1000000))
    print(f"Ending at: {endTime}")
    print(f"Elapsed time: {endTime - startTime}")

# Main part of the script
if __name__ == "__main__":
    import time
    V = 5  # Number of nodes
    
    # Initialize adjacency matrix with all zeros
    adj_matrix = [[0] * V for _ in range(V)] #CG the * symbol creates a list with [0] repeated V times, this list is created for _ = 0 to 4 times for a total of 5 rows

    # Add edges to create a graph with a disconnected node (node 4)
    add_edge(adj_matrix, 0, 1) #CG adds an edge between 0 and 1 in both directions
    add_edge(adj_matrix, 0, 2) 
    add_edge(adj_matrix, 1, 3)
    add_edge(adj_matrix, 2, 3)

    # Display the adjacency matrix
    display_matrix(adj_matrix)

    # Create and display the adjacency list
    adj_list = create_adj_list(adj_matrix)
    display_list(adj_list)
    
    # Perform and display the Depth First Search traversal
    dfs_traversal(adj_list, 0)
    
    # Perform and display the Depth First Search traversal using the adjacency matrix
    dfs_traversal_matrix(adj_matrix, 0)