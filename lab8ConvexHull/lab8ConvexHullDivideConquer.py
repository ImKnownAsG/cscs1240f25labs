POINTS = [
    (0, 3), (1, 1), (2, 2), (4, 4),
    (0, 0), (1, 2), (3, 1), (3, 3)
]

def orientation(p, q, r):
    """
    Finds the orientation of the ordered triplet (p, q, r) using the cross product.
    :returns: 0 (Collinear), 1 (Clockwise/Right), 2 (Counter-clockwise/Left)
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - \
          (q[0] - p[0]) * (r[1] - q[1])

    if val == 0:
        return 0  # Collinear
    return 1 if val > 0 else 2  # Clockwise (1) or Counter-clockwise (2)

# ----------------------------------------------------------------------
# MERGE FUNCTIONS
# ----------------------------------------------------------------------

def find_tangent(left_hull, right_hull, upper=True):
    """
    Finds the upper or lower tangent between two CCW-ordered convex hulls.
    Returns (left_index, right_index) of the tangent points.
    """
    n_l = len(left_hull)
    n_r = len(right_hull)
    
    # 1. Initialization: Find the x-extreme points' indices
    # Rightmost on Left Hull, Leftmost on Right Hull
    l = left_hull.index(max(left_hull, key=lambda p: p[0]))
    r = right_hull.index(min(right_hull, key=lambda p: p[0]))
    
    changed = True
    
    tangent_type = "Upper" if upper else "Lower"
    print(f"\n    Searching {tangent_type} Tangent from L{left_hull[l]} to R{right_hull[r]}.")

    while changed:
        changed = False
        
        # --- 1. Walk the Right Hull (R) ---
        # R walk is CW for Upper Tangent, CCW for Lower Tangent
        while True:
            # CW step (upper) or CCW step (lower)
            r_next = (r - 1 + n_r) % n_r if upper else (r + 1) % n_r
            o = orientation(left_hull[l], right_hull[r], right_hull[r_next])
            
            comparison_str = f"      R Walk: Compare L{left_hull[l]}, R{right_hull[r]}, R_next{right_hull[r_next]}. Result: {'CW' if o==1 else 'CCW' if o==2 else 'Collinear'}"

            # Upper: Continue if turn is CW (1). Lower: Continue if turn is CCW (2).
            if (upper and o == 1) or (not upper and o == 2):
                r = r_next
                changed = True
                print(f"{comparison_str}. Decision: Move R to {right_hull[r]} (improves tangent).")
            else:
                print(f"{comparison_str}. Decision: Stop R walk. Tangent found at {right_hull[r]}.")
                break

        # --- 2. Walk the Left Hull (L) ---
        # L walk is CCW for Upper Tangent, CW for Lower Tangent
        while True:
            # CCW step (upper) or CW step (lower)
            l_next = (l + 1) % n_l if upper else (l - 1 + n_l) % n_l
            o = orientation(left_hull[l_next], left_hull[l], right_hull[r])

            comparison_str = f"      L Walk: Compare L_prev{left_hull[l_next]}, L{left_hull[l]}, R{right_hull[r]}. Result: {'CW' if o==1 else 'CCW' if o==2 else 'Collinear'}"
            
            # Upper: Continue if turn is CCW (2). Lower: Continue if turn is CW (1).
            if (upper and o == 2) or (not upper and o == 1):
                l = l_next
                changed = True
                print(f"{comparison_str}. Decision: Move L to {left_hull[l]} (improves tangent).")
            else:
                print(f"{comparison_str}. Decision: Stop L walk. Tangent found at {left_hull[l]}.")
                break
            
    return l, r

def merge_hulls(left_hull, right_hull):
    """Merges two convex hulls by finding and connecting the upper and lower tangents."""
    
    print("\n  -- MERGING HULLS --")
    print(f"    Left Hull: {left_hull}")
    print(f"    Right Hull: {right_hull}")
    
    # 1. Find the upper tangent
    l_upper_idx, r_upper_idx = find_tangent(left_hull, right_hull, upper=True)
    l_upper = left_hull[l_upper_idx]
    r_upper = right_hull[r_upper_idx]
    print(f"\n  RESULT: Upper Tangent found: {l_upper} (Left) to {r_upper} (Right)")

    # 2. Find the lower tangent
    l_lower_idx, r_lower_idx = find_tangent(left_hull, right_hull, upper=False)
    l_lower = left_hull[l_lower_idx]
    r_lower = right_hull[r_lower_idx]
    print(f"\n  RESULT: Lower Tangent found: {l_lower} (Left) to {r_lower} (Right)")

    # 3. Construct the new hull (following CCW path)
    merged_hull = []
    
    # Left part: Walk from L_lower to L_upper (CCW on the left hull means decreasing index)
    curr = l_lower_idx
    while True:
        merged_hull.append(left_hull[curr])
        if curr == l_upper_idx:
            break
        curr = (curr - 1 + len(left_hull)) % len(left_hull)

    # Right part: Walk from R_upper to R_lower (CCW on the right hull means increasing index)
    curr = r_upper_idx
    while True:
        merged_hull.append(right_hull[curr])
        if curr == r_lower_idx:
            break
        curr = (curr + 1) % len(right_hull)

    print(f"\n  RESULT: Merged Hull: {merged_hull}")
    return merged_hull

# ----------------------------------------------------------------------
# DIVIDE AND CONQUER RECURSIVE FUNCTION
# ----------------------------------------------------------------------

def divide_and_conquer_convex_hull_recursive(points):
    """
    Recursive function to find the convex hull of a sorted point set.
    """
    n = len(points)
    
    # Base case: 3 or fewer points, ensure CCW order
    if n <= 3:
        if n == 3 and orientation(points[0], points[1], points[2]) == 1:
            points[1], points[2] = points[2], points[1] # Swap to make it CCW
        print(f"\nBASE CASE: Hull found: {points}")
        return points

    # Recursive step: Divide the set
    mid = n // 2
    left = points[:mid]
    right = points[mid:]
    
    print(f"\nDIVIDE: Left: {left} | Right: {right}")

    # Conquer: Find hull for each half
    left_hull = divide_and_conquer_convex_hull_recursive(left)
    right_hull = divide_and_conquer_convex_hull_recursive(right)

    # Combine: Merge the two hulls
    return merge_hulls(left_hull, right_hull)

# ----------------------------------------------------------------------
# MAIN FUNCTION
# ----------------------------------------------------------------------

def divide_and_conquer_convex_hull(points):
    """
    Calculates the Convex Hull using the Divide and Conquer Algorithm.
    """
    print("===================================================================")
    print("                DIVIDE AND CONQUER ALGORITHM")
    print("===================================================================")
    
    # Initial step: Sort points by x-coordinate (crucial for dividing)
    points.sort(key=lambda p: p[0])
    print(f"Initial X-Sorted Points Set: {points}")
    
    hull = divide_and_conquer_convex_hull_recursive(points)
    
    print("\n===================================================================")
    print(f"FINAL RESULT (Divide & Conquer): {hull}")
    print("===================================================================")
    return hull

# Execute the algorithm
divide_and_conquer_convex_hull(POINTS)