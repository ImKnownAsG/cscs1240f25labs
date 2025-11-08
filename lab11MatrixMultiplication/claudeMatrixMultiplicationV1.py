import numpy as np
import time

def naive_matrix_multiply(A, B, verbose=True):
    """
    Naive O(n^3) matrix multiplication using the 'school' method.
    
    Args:
        A: First matrix (m x n)
        B: Second matrix (n x p)
        verbose: Whether to print step-by-step information
    
    Returns:
        Result matrix C (m x p)
    """
    if verbose:
        print("\n=== NAIVE MATRIX MULTIPLICATION ===")
        print(f"Matrix A shape: {A.shape}")
        print(f"Matrix B shape: {B.shape}")
    
    # Edge case: Check dimensions compatibility
    if A.shape[1] != B.shape[0]:
        raise ValueError(f"Incompatible dimensions: A is {A.shape}, B is {B.shape}. "
                        f"A's columns ({A.shape[1]}) must equal B's rows ({B.shape[0]})")
    
    m, n = A.shape[0], A.shape[1]
    p = B.shape[1]
    
    # Initialize result matrix with zeros
    C = np.zeros((m, p))
    
    if verbose:
        print(f"Computing C ({m}x{p}) = A ({m}x{n}) × B ({n}x{p})")
        print("Using formula: C[i][j] = Σ(A[i][k] × B[k][j]) for k=0 to n-1\n")
    
    # Triple nested loop - the 'school' method
    for i in range(m):
        for j in range(p):
            if verbose and m <= 4 and p <= 4:  # Only show details for small matrices
                print(f"Computing C[{i}][{j}]:", end=" ")
            
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
                
                if verbose and m <= 4 and p <= 4:
                    print(f"A[{i}][{k}]*B[{k}][{j}]", end="")
                    if k < n - 1:
                        print(" + ", end="")
            
            if verbose and m <= 4 and p <= 4:
                print(f" = {C[i][j]}")
    
    return C


def strassen_matrix_multiply(A, B, verbose=True, depth=0):
    """
    Strassen's algorithm for matrix multiplication - O(n^2.807).
    Works on square matrices where dimensions are powers of 2.
    
    Args:
        A: First matrix (n x n, where n is a power of 2)
        B: Second matrix (n x n, where n is a power of 2)
        verbose: Whether to print step-by-step information
        depth: Recursion depth (used for indentation in verbose mode)
    
    Returns:
        Result matrix C (n x n)
    """
    indent = "  " * depth
    
    # Edge case: Check if matrices are square
    if A.shape[0] != A.shape[1] or B.shape[0] != B.shape[1]:
        raise ValueError(f"Strassen requires square matrices. Got A: {A.shape}, B: {B.shape}")
    
    # Edge case: Check if dimensions match
    if A.shape != B.shape:
        raise ValueError(f"Matrices must have same dimensions. Got A: {A.shape}, B: {B.shape}")
    
    n = A.shape[0]
    
    # Edge case: Check if dimension is power of 2
    if n & (n - 1) != 0:
        raise ValueError(f"Strassen requires matrix dimension to be a power of 2. Got: {n}")
    
    if verbose and depth == 0:
        print("\n=== STRASSEN'S MATRIX MULTIPLICATION ===")
        print(f"Matrix dimensions: {n}x{n}")
        print("Strassen uses 7 multiplications instead of 8 for divide-and-conquer\n")
    
    # Base case: Use naive multiplication for small matrices
    if n <= 2:
        if verbose:
            print(f"{indent}Base case reached (n={n}), using naive multiplication")
        return naive_matrix_multiply(A, B, verbose=False)
    
    if verbose:
        print(f"{indent}Dividing {n}x{n} matrices into four {n//2}x{n//2} submatrices")
    
    # Divide matrices into quadrants
    mid = n // 2
    A11, A12 = A[:mid, :mid], A[:mid, mid:]
    A21, A22 = A[mid:, :mid], A[mid:, mid:]
    B11, B12 = B[:mid, :mid], B[:mid, mid:]
    B21, B22 = B[mid:, :mid], B[mid:, mid:]
    
    if verbose:
        print(f"{indent}Computing 7 Strassen products (M1 through M7)...")
    
    # Compute the 7 Strassen products
    if verbose:
        print(f"{indent}M1 = (A11 + A22) × (B11 + B22)")
    M1 = strassen_matrix_multiply(A11 + A22, B11 + B22, verbose=False, depth=depth+1)
    
    if verbose:
        print(f"{indent}M2 = (A21 + A22) × B11")
    M2 = strassen_matrix_multiply(A21 + A22, B11, verbose=False, depth=depth+1)
    
    if verbose:
        print(f"{indent}M3 = A11 × (B12 - B22)")
    M3 = strassen_matrix_multiply(A11, B12 - B22, verbose=False, depth=depth+1)
    
    if verbose:
        print(f"{indent}M4 = A22 × (B21 - B11)")
    M4 = strassen_matrix_multiply(A22, B21 - B11, verbose=False, depth=depth+1)
    
    if verbose:
        print(f"{indent}M5 = (A11 + A12) × B22")
    M5 = strassen_matrix_multiply(A11 + A12, B22, verbose=False, depth=depth+1)
    
    if verbose:
        print(f"{indent}M6 = (A21 - A11) × (B11 + B12)")
    M6 = strassen_matrix_multiply(A21 - A11, B11 + B12, verbose=False, depth=depth+1)
    
    if verbose:
        print(f"{indent}M7 = (A12 - A22) × (B21 + B22)")
    M7 = strassen_matrix_multiply(A12 - A22, B21 + B22, verbose=False, depth=depth+1)
    
    if verbose:
        print(f"{indent}Combining products to form result quadrants...")
    
    # Combine the products to get the result quadrants
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6
    
    # Combine quadrants into final result
    C = np.vstack([np.hstack([C11, C12]), np.hstack([C21, C22])])
    
    if verbose and depth == 0:
        print(f"{indent}Strassen multiplication complete!")
    
    return C


def pad_matrix_to_power_of_2(matrix):
    """
    Pad a matrix with zeros to make its dimensions a power of 2.
    This is necessary for Strassen's algorithm.
    
    Args:
        matrix: Input matrix
    
    Returns:
        Padded matrix and original dimensions
    """
    m, n = matrix.shape
    # Find the next power of 2
    size = max(m, n)
    next_pow2 = 2 ** int(np.ceil(np.log2(size)))
    
    print(f"Original dimensions: {m}x{n}")
    print(f"Padding to: {next_pow2}x{next_pow2} (next power of 2)")
    
    padded = np.zeros((next_pow2, next_pow2))
    padded[:m, :n] = matrix
    
    return padded, (m, n)


# ============ DEMONSTRATION ============

print("=" * 60)
print("MATRIX MULTIPLICATION COMPARISON")
print("=" * 60)

# Test 1: Small matrix (4x4) - shows detailed steps
print("\n" + "=" * 60)
print("TEST 1: Small 4x4 matrices (detailed output)")
print("=" * 60)

A_small = np.array([[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9, 10, 11, 12],
                     [13, 14, 15, 16]])

B_small = np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

print("\nMatrix A:")
print(A_small)
print("\nMatrix B (Identity):")
print(B_small)

result_naive = naive_matrix_multiply(A_small, B_small, verbose=True)
print("\nResult (Naive):")
print(result_naive)

result_strassen = strassen_matrix_multiply(A_small, B_small, verbose=True)
print("\nResult (Strassen):")
print(result_strassen)

print("\nVerification: Results match?", np.allclose(result_naive, result_strassen))


# Test 2: Performance comparison (8x8)
print("\n" + "=" * 60)
print("TEST 2: Performance comparison on 8x8 matrices")
print("=" * 60)

np.random.seed(42)
A_large = np.random.rand(8, 8)
B_large = np.random.rand(8, 8)

print("\nTesting with random 8x8 matrices...")

start = time.time()
result_naive_large = naive_matrix_multiply(A_large, B_large, verbose=False)
naive_time = time.time() - start

start = time.time()
result_strassen_large = strassen_matrix_multiply(A_large, B_large, verbose=False)
strassen_time = time.time() - start

print(f"\nNaive method time: {naive_time:.6f} seconds")
print(f"Strassen method time: {strassen_time:.6f} seconds")
print(f"Results match? {np.allclose(result_naive_large, result_strassen_large)}")


# Test 3: Edge cases
print("\n" + "=" * 60)
print("TEST 3: Edge Cases")
print("=" * 60)

print("\n1. Non-square matrices (Naive only):")
A_rect = np.array([[1, 2, 3], [4, 5, 6]])  # 2x3
B_rect = np.array([[1, 2], [3, 4], [5, 6]])  # 3x2
result_rect = naive_matrix_multiply(A_rect, B_rect, verbose=True)
print("Result:")
print(result_rect)

print("\n2. Incompatible dimensions (will raise error):")
try:
    A_bad = np.array([[1, 2], [3, 4]])  # 2x2
    B_bad = np.array([[1, 2, 3]])  # 1x3
    naive_matrix_multiply(A_bad, B_bad)
except ValueError as e:
    print(f"Error caught (expected): {e}")

print("\n3. Non-power-of-2 dimensions for Strassen:")
try:
    A_odd = np.random.rand(5, 5)
    B_odd = np.random.rand(5, 5)
    strassen_matrix_multiply(A_odd, B_odd)
except ValueError as e:
    print(f"Error caught (expected): {e}")
    print("\nSolution: Pad the matrix to next power of 2")
    A_padded, orig_dims = pad_matrix_to_power_of_2(A_odd)
    B_padded, _ = pad_matrix_to_power_of_2(B_odd)
    result_padded = strassen_matrix_multiply(A_padded, B_padded, verbose=False)
    # Extract the original size result
    result_unpadded = result_padded[:orig_dims[0], :orig_dims[1]]
    print(f"Successfully computed result (extracted to {orig_dims[0]}x{orig_dims[1]})")

print("\n" + "=" * 60)
print("KEY TAKEAWAYS FOR YOUR ASSIGNMENT:")
print("=" * 60)
print("""
1. NAIVE METHOD (School method):
   - Time complexity: O(n³) - three nested loops
   - Works with any matrix dimensions (m×n) × (n×p)
   - Simple to understand and implement
   - Best for small matrices or when simplicity matters

2. STRASSEN'S METHOD:
   - Time complexity: O(n^2.807) - faster for large matrices
   - Requires square matrices with power-of-2 dimensions
   - Uses divide-and-conquer with 7 multiplications instead of 8
   - Better for large matrices but has overhead for small ones

3. EDGE CASES TO REMEMBER:
   - Check dimension compatibility: A's columns must equal B's rows
   - Strassen requires square matrices
   - Strassen requires dimensions to be powers of 2 (pad if needed)
   - For very small matrices, naive method may actually be faster
   - Consider numerical stability with Strassen (more additions/subtractions)
""")