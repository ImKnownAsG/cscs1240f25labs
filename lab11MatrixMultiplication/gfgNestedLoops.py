def multiply(mat1, mat2):
    n = len(mat1)
    m = len(mat1[0])
    q = len(mat2[0])

    # Initialize the result matrix with 
    # dimensions n×q, filled with 0s
    res = [[0 for _ in range(q)] for _ in range(n)]

    # Loop through each row of mat1
    for i in range(n):

        # Loop through each column of mat2
        for j in range(q):

            # Compute the dot product of 
            # row mat1[i] and column mat2[][j]
            for k in range(m):
                res[i][j] += mat1[i][k] * mat2[k][j]

    return res

if __name__ == "__main__":
    
    mat1 = [[1, 2, 3],[4, 5, 6]]
    mat2 = [[7, 8],[9, 10],[11, 12]]

    res = multiply(mat1, mat2)

    for row in res:
        for val in row:
            print(val, end=" ")
        print()