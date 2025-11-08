# Fixed set of points for demonstration
#POINTS = [
#    (0, 3), (1, 1), (2, 2), (4, 4),
#    (0, 0), (1, 2), (3, 1), (3, 3)
#]

def orientation(p, q, r):
    """
    Finds the orientation of the ordered triplet (p, q, r).
    The value of the expression (q_y - p_y) * (r_x - q_x) -
    (q_x - p_x) * (r_y - q_y) is used.

    :returns:
      0: Collinear (p, q, r are on the same line)
      1: Clockwise (Right turn)
      2: Counter-clockwise (Left turn)
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - \
          (q[0] - p[0]) * (r[1] - q[1])

    if val == 0:
        return 0  # Collinear
    return 1 if val > 0 else 2  # Clockwise (1) or Counter-clockwise (2)


def jarvis_march_convex_hull(points):
    """
    Calculates the Convex Hull using Jarvis's March (Gift Wrapping) Algorithm.
    Prints step-by-step comparisons.
    """
    print("===================================================================")
    print("               JARVIS'S MARCH (GIFT WRAPPING) ALGORITHM")
    print("===================================================================")
    print(f"Initial Points Set: {points}")
    n = len(points)
    if n < 3:
        return points

    # Find the leftmost point (guaranteed to be on the hull)
    l = min(range(n), key=lambda i: points[i])
    hull = []
    p = l
    
    print(f"\nSTART: Initial hull point (leftmost) found: P{p} {points[p]}")

    while True:
        # Add current point to hull
        hull.append(points[p])
        
        # q is the index of the next point
        q = (p + 1) % n
        
        print(f"\nCURRENT HULL: {hull}")
        print(f"  Starting from point P{p} {points[p]}. Candidate for next point P{q} {points[q]}")

        # Iterate through all points to find the 'most counter-clockwise' one
        for i in range(n):
            if i == p: continue
            
            # Compare current 'best' next point (q) with point i
            turn = orientation(points[p], points[q], points[i])
            
            comparison_str = f"  Compare P{p} {points[p]}, P{q} {points[q]}, P{i} {points[i]}"
            
            if turn == 2: # Counter-clockwise turn (Left) -> point i is a better candidate
                print(f"{comparison_str}: CCW (Left Turn). New candidate P{i} is better.")
                q = i
            elif turn == 1: # Clockwise turn (Right) -> point q remains better
                print(f"{comparison_str}: CW (Right Turn). P{q} remains the candidate.")
            elif turn == 0: # Collinear -> check distance
                 # For simplicity, usually we take the furthest collinear point,
                 # but for this basic demonstration, we stick to the orientation check.
                 print(f"{comparison_str}: COLLINEAR. P{q} remains the candidate.")

        # q is now the index of the point that forms the smallest CCW turn
        # with the current hull edge, meaning it's the next point on the hull.
        print(f"  DECISION: The next point on the hull is P{q} {points[q]}")
        p = q

        # Stop when we return to the starting point
        if p == l:
            break

    print(f"\nFINAL RESULT (Jarvis's March): {hull}")
    return hull

jarvis_march_convex_hull([
    (0, 3), (1, 1), (2, 2), (4, 4),
    (0, 0), (1, 2), (3, 1), (3, 3)
])


import math

def dist_sq(p1, p2):
    """Calculates squared distance between two points."""
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def polar_angle_comparator(p1, p2):
    """
    Custom comparison for sorting points by polar angle with respect to P0.
    Returns -1 if p1 < p2, 1 if p1 > p2, 0 if equal.
    """
    p0 = graham_scan_convex_hull.P0

    # 1. Orientation check
    o = orientation(p0, p1, p2)

    if o == 0:
        # 2. Collinear: Closer point comes first
        d1 = dist_sq(p0, p1)
        d2 = dist_sq(p0, p2)
        return -1 if d1 <= d2 else 1
    
    # 3. CCW (2) comes before CW (1)
    return -1 if o == 2 else 1


def graham_scan_convex_hull(points):
    """
    Calculates the Convex Hull using Graham Scan Algorithm.
    Prints step-by-step comparisons.
    """
    print("\n\n===================================================================")
    print("                      GRAHAM SCAN ALGORITHM")
    print("===================================================================")
    print(f"Initial Points Set: {points}")
    n = len(points)
    if n < 3:
        return points

    # Step 1: Find the bottom-most, then leftmost point (P0)
    p0 = min(points, key=lambda p: (p[1], p[0]))
    graham_scan_convex_hull.P0 = p0 # Store as a reference for the comparator

    # Step 2: Sort the remaining points by polar angle with P0
    # Python's `sort` with a custom `key` is often used, but to mimic
    # a proper comparison-based sort, we use a manual implementation or
    # a wrapper that uses functools.cmp_to_key (simpler for display).
    from functools import cmp_to_key
    
    # Separate P0 and sort the rest
    points.remove(p0)
    
    # Sort with the custom comparator
    sorted_points = sorted(points, key=cmp_to_key(polar_angle_comparator))
    
    # Put P0 back at the start
    points = [p0] + sorted_points
    n = len(points)

    print(f"\nSTEP 1 & 2: Sorted points (by polar angle w.r.t P0 {p0}): {points}")
    
    # Remove collinear points that aren't the farthest
    final_points = [points[0]]
    i = 1
    while i < n:
        j = i + 1
        while j < n and orientation(points[0], points[i], points[j]) == 0:
            j += 1
        final_points.append(points[j-1])
        i = j
    
    if len(final_points) < 3:
        return final_points
    
    points = final_points
    n = len(points)
    
    # Step 3: Initialize the stack (hull)
    stack = [points[0], points[1], points[2]]
    print(f"\nSTEP 3: Initial stack: {stack}")

    # Step 4: Process remaining points
    for i in range(3, n):
        p_i = points[i]
        
        print(f"\nProcessing point P{i} {p_i}")
        
        while len(stack) >= 2:
            p_top = stack[-1]
            p_next_to_top = stack[-2]
            
            turn = orientation(p_next_to_top, p_top, p_i)
            
            comparison_str = f"  Compare {p_next_to_top}, {p_top}, {p_i}"
            
            if turn == 2: # CCW (Left turn): Hull is convex. Push p_i and break inner loop.
                print(f"{comparison_str}: CCW (Left Turn). Add point P{i} to stack.")
                break
            
            elif turn == 1: # CW (Right turn): Concave bend. Pop top point.
                print(f"{comparison_str}: CW (Right Turn). POP {p_top} (inside hull).")
                stack.pop()
                
            elif turn == 0: # Collinear: Check if p_i is closer or farther than p_top
                print(f"{comparison_str}: COLLINEAR. POP {p_top} (inside hull).")
                stack.pop()

        stack.append(p_i)


    print(f"\nFINAL RESULT (Graham Scan): {stack}")
    return stack

graham_scan_convex_hull([
    (0, 3), (1, 1), (2, 2), (4, 4),
    (0, 0), (1, 2), (3, 1), (3, 3)
])


# Function to calculate the cross product (used for orientation)
def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

# Assuming orientation(p, q, r) returns 0 (Collinear), 1 (CW), 2 (CCW)

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
    
    print(f"\n    Starting tangent search from: L{left_hull[l]}, R{right_hull[r]} (Upper={upper})")

    while changed:
        changed = False
        
        # --- 1. Walk the Right Hull (R) ---
        while True:
            # R_next is CW for Upper Tangent walk, CCW for Lower Tangent walk
            r_next = (r - 1 + n_r) % n_r if upper else (r + 1) % n_r 
            o = orientation(left_hull[l], right_hull[r], right_hull[r_next])
            
            # Continue if the turn is "good" (outside the hull)
            # Upper: Continue if CW (1). Lower: Continue if CCW (2).
            if (upper and o == 1) or (not upper and o == 2):
                r = r_next
                changed = True
                print(f"      R Walk: Continuing walk. New candidate: {right_hull[r]}")
            else:
                print(f"      R Walk: Stop walk. Tangent point R found: {right_hull[r]}")
                break

        # --- 2. Walk the Left Hull (L) ---
        while True:
            # L_next is CCW for Upper Tangent walk, CW for Lower Tangent walk
            l_next = (l + 1) % n_l if upper else (l - 1 + n_l) % n_l
            o = orientation(left_hull[l_next], left_hull[l], right_hull[r])

            # Continue if the turn is "good" (outside the hull)
            # Upper: Continue if CCW (2). Lower: Continue if CW (1).
            if (upper and o == 2) or (not upper and o == 1):
                l = l_next
                changed = True
                print(f"      L Walk: Continuing walk. New candidate: {left_hull[l]}")
            else:
                print(f"      L Walk: Stop walk. Tangent point L found: {left_hull[l]}")
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
    print(f"  Upper Tangent found: {l_upper} (Left) to {r_upper} (Right)")

    # 2. Find the lower tangent
    l_lower_idx, r_lower_idx = find_tangent(left_hull, right_hull, upper=False)
    l_lower = left_hull[l_lower_idx]
    r_lower = right_hull[r_lower_idx]
    print(f"  Lower Tangent found: {l_lower} (Left) to {r_lower} (Right)")

    # 3. Construct the new hull (following CCW path)
    merged_hull = []
    
    # Left part: Walk from L_lower to L_upper (CCW walk on the hull is *decreasing* index)
    curr = l_lower_idx
    while True:
        merged_hull.append(left_hull[curr])
        if curr == l_upper_idx:
            break
        curr = (curr - 1 + len(left_hull)) % len(left_hull)

    # Right part: Walk from R_upper to R_lower (CCW walk on the hull is *increasing* index)
    curr = r_upper_idx
    while True:
        merged_hull.append(right_hull[curr])
        if curr == r_lower_idx:
            break
        curr = (curr + 1) % len(right_hull)

    print(f"  Merged Hull: {merged_hull}")
    return merged_hull

def divide_and_conquer_convex_hull_recursive(points):
    """
    Recursive function to find the convex hull of a sorted point set.
    """
    n = len(points)
    
    # Base case: 3 or fewer points, ensure CCW order
    if n <= 3:
        if n == 3 and orientation(points[0], points[1], points[2]) == 1:
            points[1], points[2] = points[2], points[1] # Swap to make it CCW
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

def divide_and_conquer_convex_hull(points):
    """
    Calculates the Convex Hull using the Divide and Conquer Algorithm.
    Prints step-by-step comparisons.
    """
    print("\n\n===================================================================")
    print("                DIVIDE AND CONQUER ALGORITHM")
    print("===================================================================")
    
    # Initial step: Sort points by x-coordinate
    print(f'Points before the sort: {points}')
    points.sort(key=lambda p: p[0])
    print(f"Initial X-Sorted Points Set: {points}")
    
    hull = divide_and_conquer_convex_hull_recursive(points)
    
    print(f"\nFINAL RESULT (Divide & Conquer): {hull}")
    return hull

divide_and_conquer_convex_hull([
    (0, 3), (1, 1), (2, 2), (4, 4),
    (0, 0), (1, 2), (3, 1), (3, 3)
])