import sys

# Define the number of nodes
NUM_NODES = 7
# Set a value for infinity to represent no edge in the matrix
INF = sys.maxsize

class DisjointSet:
    """
    Implements the Union-Find data structure with path compression and union by rank.
    This is essential for the efficiency of Kruskal's algorithm.
    """
    def __init__(self, n):
        # Parent array: parent[i] is the parent of element i
        self.parent = list(range(n))
        # Rank array: used to keep the tree flat (union by rank)
        self.rank = [0] * n

    def find(self, i):
        """
        Finds the representative (root) of the set containing element i
        with path compression.
        """
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i]) # Path compression
        return self.parent[i]

    def union(self, i, j):
        """
        Unites the set that contains i and the set that contains j
        using union by rank. Returns True if a union was performed (no cycle),
        False otherwise (cycle detected).
        """
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # Attach smaller rank tree under root of high rank tree (Union by Rank)
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True # Union successful
        return False # Cycle detected

def kruskals_mst(edges, num_nodes):
    """
    Implements Kruskal's algorithm to find the Minimum Spanning Tree (MST).

    Args:
        edges (list): A list of tuples (u, v, weight) representing the graph edges.
        num_nodes (int): The number of nodes in the graph.

    Returns:
        tuple: A tuple containing (mst_edges, mst_weight).
    """
    # 1. Sort all the edges in non-decreasing order of their weight
    sorted_edges = sorted(edges, key=lambda item: item[2])

    mst_edges = []
    mst_weight = 0
    ds = DisjointSet(num_nodes)

    # 2. Iterate through the sorted edges
    for u, v, weight in sorted_edges:
        # Check if including this edge (u, v) creates a cycle
        if ds.find(u) != ds.find(v):
            # No cycle detected, include the edge in the MST
            ds.union(u, v)
            mst_edges.append((u, v, weight))
            mst_weight += weight

            # Stop when MST has num_nodes - 1 edges
            if len(mst_edges) == num_nodes - 1:
                break

    return mst_edges, mst_weight

def edges_to_adjacency_matrix(edges, num_nodes, default_value=INF):
    """
    Converts a list of weighted edges into an adjacency matrix.
    """
    matrix = [[default_value] * num_nodes for _ in range(num_nodes)]
    for u, v, weight in edges:
        matrix[u][v] = weight
        matrix[v][u] = weight # Undirected graph
    return matrix

def display_matrix(title, matrix, num_nodes):
    """
    Prints the adjacency matrix in a readable format.
    """
    print(f"\n--- {title} ---")
    header = "    " + " ".join([f"N{i: <2}" for i in range(num_nodes)])
    print(header)
    print("  " + "-" * len(header))

    for i in range(num_nodes):
        row = f"N{i}: "
        for j in range(num_nodes):
            val = matrix[i][j]
            row += f"{val: <4}" if val != INF else "INF "
        print(row)
    print("-" * len(header))


def main():
    # Example Graph (7 Nodes: 0 to 6)
    # Edge format: (Node A, Node B, Weight)
    graph_edges = [
        (0, 1, 7), (0, 3, 5),
        (1, 2, 8), (1, 3, 9), (1, 4, 7),
        (2, 4, 5), (2, 5, 6),
        (3, 4, 15), (3, 6, 6),
        (4, 5, 8), (4, 6, 9),
        (5, 6, 11)
    ]

    print(f"Graph with {NUM_NODES} nodes defined.")
    print(f"Total Edges: {len(graph_edges)}")

    # 1. Display the initial graph as an Adjacency Matrix
    initial_matrix = edges_to_adjacency_matrix(graph_edges, NUM_NODES, default_value=INF)
    display_matrix("Initial Graph Adjacency Matrix (Weights)", initial_matrix, NUM_NODES)
    # The diagonal (i, i) remains INF, but for a true adjacency matrix, this is often 0.
    # We keep it as INF here to clearly distinguish non-edges.

    # 2. Run Kruskal's MST Algorithm
'''    mst_edges, mst_weight = kruskals_mst(graph_edges, NUM_NODES)

    print("\n--- Kruskal's Algorithm Results ---")
    print("MST Edges:")
    for u, v, weight in mst_edges:
        print(f"  ({u} - {v}) with weight {weight}")
    print(f"\nTotal Minimum Spanning Tree Weight: {mst_weight}")

    # 3. Display the resulting MST as an Adjacency Matrix
    mst_matrix = edges_to_adjacency_matrix(mst_edges, NUM_NODES, default_value=0)
    display_matrix("Minimum Spanning Tree (MST) Adjacency Matrix", mst_matrix, NUM_NODES)
'''

if __name__ == "__main__":
    main()
