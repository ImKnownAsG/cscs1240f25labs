import heapq
import random

def dijkstra(graph, start_node, end_node):
    """
    Finds the minimum cost-weighted path from start_node to end_node
    in a graph using Dijkstra's algorithm.

    Args:
        graph (dict): A dictionary representing the graph where keys are nodes
                      and values are dictionaries of neighboring nodes and their weights.
        start_node: The starting node.
        end_node: The ending node.

    Returns:
        tuple: A tuple containing the shortest path as a list and its total cost.
               Returns (None, float('inf')) if no path exists.
    """
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    predecessors = {node: None for node in graph}
    priority_queue = [(0, start_node)]

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_node == end_node:
            break

        if current_cost > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            cost = current_cost + weight

            if cost < distances[neighbor]:
                distances[neighbor] = cost
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (cost, neighbor))

    path = []
    current = end_node
    while current is not None:
        path.append(current)
        current = predecessors[current]
    path.reverse()

    if path and path[0] != start_node:
        return None, float('inf')

    return path, distances[end_node]

def display_adjacency_matrix(graph, num_nodes):
    """
    Displays the graph as an adjacency matrix.

    Args:
        graph (dict): The graph represented as an adjacency list.
        num_nodes (int): The number of nodes in the graph.
    """
    matrix = [[float('inf')] * num_nodes for _ in range(num_nodes)]

#    for i in range(num_nodes):
#        matrix[i][i] = 0

    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            matrix[node][neighbor] = weight

    print("\nAdjacency Matrix:")
    # Print column headers
    print("      " + " ".join([f"{i:4d}" for i in range(num_nodes)]))
    print("      " + "-" * (num_nodes * 5 - 1))

    # Print rows
    for i in range(num_nodes):
        row_str = " ".join([f"{val:4d}" if val != float('inf') else " inf" for val in matrix[i]])
        print(f"  {i:2d} | {row_str}")

# --- Graph Setup ---
nodes = list(range(10))
graph = {node: {} for node in nodes}
for i in nodes:
    for j in nodes:
        if i != j:
            if random.randint(0, 10) > 2:
                weight = random.randint(1, 10) 
                graph[i][j] = weight
            else: #I didn't want all the nodes connected so I added this - this can result in a disconnected graph but there is an else statement for that
                graph[i][j] = float('inf')

# --- Main Execution ---
if __name__ == "__main__":
    start = 0
    end = 9

    # Display the adjacency matrix
    display_adjacency_matrix(graph, len(nodes))
    
    # Find and display the minimum cost path
    path, cost = dijkstra(graph, start, end)

    if path:
        print("\n" + "="*50)
        print(f"Minimum cost path from node {start} to node {end}:")
        print(f"Path: {' -> '.join(map(str, path))}")
        print(f"Total Cost: {cost}")
    else:
        print(f"\nNo path found from node {start} to node {end}.")