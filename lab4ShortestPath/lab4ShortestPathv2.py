import heapq
import random
import matplotlib.pyplot as plt
import networkx as nx

def dijkstra_stepped(graph, start_node, end_node):
    """
    Finds the minimum cost-weighted path and steps through the search.
    """
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    predecessors = {node: None for node in graph}
    priority_queue = [(0, start_node)]

    print("=== Dijkstra's Algorithm Step-by-Step ===")
    print(f"Starting at node {start_node}...\n")
    
    step_count = 0
    while priority_queue:
        step_count += 1
        current_cost, current_node = heapq.heappop(priority_queue)

        print(f"--- Step {step_count} ---")
        print(f"Current node: {current_node} (Cost: {current_cost})")

        if current_node == end_node:
            print(f"Target node {end_node} reached. Path found!")
            break

        if current_cost > distances[current_node]:
            print(f"  Skipping {current_node}: already found a shorter path.")
            continue

        print(f"  Exploring neighbors of {current_node}:")
        for neighbor, weight in graph[current_node].items():
            cost = current_cost + weight

            if cost < distances[neighbor]:
                print(f"    New path to {neighbor} found! Cost: {cost} (Old Cost: {distances[neighbor]})")
                distances[neighbor] = cost
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (cost, neighbor))
            else:
                print(f"    Path to {neighbor} (Cost: {cost}) is not an improvement.")
        print("")

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
    """
    matrix = [[float('inf')] * num_nodes for _ in range(num_nodes)]
    for i in range(num_nodes):
        matrix[i][i] = 0
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            matrix[node][neighbor] = weight
    print("\nAdjacency Matrix:")
    print("      " + " ".join([f"{i:4d}" for i in range(num_nodes)]))
    print("      " + "-" * (num_nodes * 5 - 1))
    for i in range(num_nodes):
        row_str = " ".join([f"{val:4d}" if val != float('inf') and val != 0 else "  --" for val in matrix[i]])
        print(f"  {i:2d} | {row_str}")

def visualize_path(graph, path, start_node, end_node):
    """
    Draws the graph and highlights the shortest path.
    """
    G = nx.DiGraph()
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)
    pos = nx.circular_layout(G)
    plt.figure(figsize=(10, 8))
    nx.draw_networkx_nodes(G, pos, node_color='lightgray', node_size=700)
    nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=1, alpha=0.5, edge_color='gray')
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=2, edge_color='red')
    nx.draw_networkx_nodes(G, pos, nodelist=[start_node], node_color='green', node_size=800)
    nx.draw_networkx_nodes(G, pos, nodelist=[end_node], node_color='blue', node_size=800)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    plt.title("Dijkstra's Algorithm - Minimum Cost Path Visualization")
    
    # Add text box with path information
    path_str = ' -> '.join(map(str, path))
    info_text = f"Path: {path_str}\nCost: {cost}"
    plt.text(0.05, 0.95, info_text, transform=plt.gca().transAxes, fontsize=10, verticalalignment='top', bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.8))
    plt.axis('off')
    plt.show()

# --- Graph Setup ---
nodes = list(range(20))
graph = {node: {} for node in nodes}
for i in nodes:
    for j in range(i + 1, len(nodes)):
        if random.randint(0, 10) > 4:
            weight = random.randint(1, 100)
            graph[i][j] = weight
            graph[j][i] = weight


# --- Main Execution ---
if __name__ == "__main__":
    start = 0
    end = 9

    display_adjacency_matrix(graph, len(nodes))
    
    path, cost = dijkstra_stepped(graph, start, end)

    if path:
        print("\n" + "="*50)
        print(f"Minimum cost path from node {start} to node {end}:")
        print(f"Path: {' -> '.join(map(str, path))}")
        print(f"Total Cost: {cost}")
        visualize_path(graph, path, start, end)
    else:
        print(f"\nNo path found from node {start} to node {end}.")
