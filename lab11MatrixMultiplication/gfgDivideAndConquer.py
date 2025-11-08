# Function to add two matrices of same dimensions r×c

def add(mat1, mat2):
    r = len(mat1)
    c = len(mat1[0])

    # Initialize result matrix with dimensions r×c
    res = [[0] * c for _ in range(r)]

    # Perform element-wise addition
    for i in range(r):
        for j in range(c):
            res[i][j] = mat1[i][j] + mat2[i][j]

    return res

# Function to multiply mat1 (n×m) with mat2 (m×q)
def multiply(mat1, mat2):
    n = len(mat1)
    m = len(mat1[0])
    q = len(mat2[0])

    # Initialize result matrix with dimensions n×q
    res = [[0] * q for _ in range(n)]

    # Matrix multiplication logic
    for i in range(n):
        for j in range(q):
            for k in range(m):
                res[i][j] += mat1[i][k] * mat2[k][j]

    return res
    
if __name__ == "__main__":
    mat1 = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    
    mat2 = [
        [7, 8],
        [9, 10],
        [11, 12]
    ]
    
    res = multiply(mat1, mat2)
    
    for row in res:
        print(" ".join(map(str, row)))
        