# Define a sample graph using an adjacency list.
# The graph is represented as a dictionary where keys are vertices (0 to 4)
# and values are lists of their neighbors.
# This specific graph (a cycle of 5 vertices with a chord, 0-1-2-3-4-0 and 1-3)
# is chosen to demonstrate the greedy algorithm's failure.
# The chromatic number (minimum colors required) for this graph is 3.
# Vertices: 0, 1, 2, 3, 4
graph = {
    0: [1, 2],
    1: [0, 2, 4],
    2: [0, 1, 4],
    3: [4],
    4: [1, 2, 3]
}
num_vertices = len(graph)

# --- Backtracking (m-Coloring Decision Problem and Optimization) ---

def is_safe(v, colors, c):
    """
    Checks if assigning a color 'c' to vertex 'v' is valid.
    It's safe if 'v' has no neighbor 'u' that is already assigned color 'c'.
    """
    for neighbor in graph[v]:
        if colors[neighbor] == c:
            return False
    return True

def graph_coloring_backtracking_util(m, colors, v):
    """
    A utility function using backtracking to solve the m-coloring problem.
    It attempts to color the graph with at most 'm' colors starting from vertex 'v'.

    :param m: The maximum number of colors allowed.
    :param colors: A list/array storing the color assigned to each vertex.
                   colors[i] = 0 means vertex i is uncolored.
    :param v: The current vertex to be colored.
    :return: True if a solution is found, False otherwise.
    """
    # Base case: If all vertices are colored, a solution is found
    if v == num_vertices:
        return True

    # Try all 'm' colors for the current vertex 'v'
    for c in range(1, m + 1):  # Colors are represented by integers 1 to m
        if is_safe(v, colors, c):
            # Assign the color
            colors[v] = c

            # Recur for the next vertex
            if graph_coloring_backtracking_util(m, colors, v + 1):
                return True

            # If assigning color 'c' doesn't lead to a solution, backtrack
            # Reset the color (implicitly done by the next iteration of the loop
            # or by the return False, but we explicitly reset for clarity)
            colors[v] = 0

    # If no color can be assigned to this vertex, return False
    return False

def find_min_colors_backtracking(max_m=num_vertices):
    """
    Finds the minimum number of colors required (Chromatic Number)
    by trying m = 1, 2, 3, ... until a solution is found.
    """
    print("Starting backtracking search for minimum colors...")
    for m in range(1, max_m + 1):
        # Initialize colors: 0 means uncolored
        colors = [0] * num_vertices
        
        # Try to color the graph with 'm' colors
        if graph_coloring_backtracking_util(m, colors, 0):
            return m, colors
            
    return -1, [] # Should not happen for a valid graph

# --- Greedy Coloring Algorithm ---

def greedy_coloring():
    """
    Implements the simple greedy coloring algorithm.
    It iterates through vertices and assigns the smallest available color.

    :return: A tuple of (number_of_colors_used, colors_assigned)
    """
    # Initialize a list to store the color assigned to each vertex.
    # colors[i] is the color of vertex i. -1 means uncolored.
    colors = [-1] * num_vertices
    
    # Assign the first color (color 1) to the first vertex (vertex 0)
    colors[0] = 1
    
    # Keep track of the maximum color used
    max_color_used = 1

    # Process all other vertices one by one
    for v in range(1, num_vertices):
        # Set to store colors of the adjacent vertices
        neighbor_colors = set()
        for neighbor in graph[v]:
            if colors[neighbor] != -1: # Only consider colored neighbors
                neighbor_colors.add(colors[neighbor])
        
        # Find the smallest available color (1, 2, 3, ...)
        color_to_assign = 1
        while color_to_assign in neighbor_colors:
            color_to_assign += 1
        
        # Assign the smallest available color
        colors[v] = color_to_assign
        
        # Update the maximum color used
        max_color_used = max(max_color_used, color_to_assign)
        
    return max_color_used, colors

# --- Demonstration ---

print("## 🧪 Demonstration of Greedy vs. Backtracking")
print(f"Graph with {num_vertices} vertices: {graph}")
print("-" * 50)

# 1. Run the Greedy Algorithm
greedy_colors_used, greedy_assignment = greedy_coloring()

print(f"### 🎯 Greedy Coloring Result")
print(f"Number of colors found by Greedy: **{greedy_colors_used}**")
print(f"Color assignment (Vertex: Color): {list(zip(range(num_vertices), greedy_assignment))}")

print("\n> **Observation:** The greedy algorithm assigned 4 colors. It failed to find the optimal solution because it makes locally optimal choices (smallest available color) which can lead to conflicts requiring more colors later.")
print("-" * 50)

# 2. Run the Backtracking Algorithm to find the true minimum
min_colors_required, min_assignment = find_min_colors_backtracking()

print(f"### ✨ Backtracking Minimum Colors (Chromatic Number)")
print(f"Minimum number of colors found by Backtracking: **{min_colors_required}**")
print(f"Optimal color assignment (Vertex: Color): {list(zip(range(num_vertices), min_assignment))}")
print("\n> **Observation:** The backtracking algorithm correctly found the **minimum** number of colors (the chromatic number), which is 3, by exploring all possibilities until a valid assignment with the minimum color count was achieved.")
print("-" * 50)