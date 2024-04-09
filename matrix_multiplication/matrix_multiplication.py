# Sum a list of matrices
def matrix_sum(*M: list[list[list[int]]]) -> list[list[int]]:
    n = len(M)
    y = len(M[0])
    x = len(M[0][0])

    return [ [ sum([ M[l][i][j] for l in range(n) ]) for j in range(x) ] for i in range(y) ]

# Multiply a matrix by a scalar
def matrix_scalar_mul(M: list[list[int]], S: int) -> list[list[int]]:
    return [ [ v*S for v in R ] for R in M ]

# Get negative matrix (multiply by -1)
def matrix_neg(M: list[list[int]]):
    return matrix_scalar_mul(M, -1)

# Multiply two matrices using the iterative method
def matrix_mul_iter(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][0]*B[0][j]
            for k in range(1, n):
                C[i][j] += A[i][k]*B[k][j]
    
    return C

# Split a matrix into 4 quadrants
def split_quadrants(M: list[list[int]]) -> list[list[list[int]]]:
    n = len(M) # n is a power of 2, n > 1
    n2 = int(n/2)

    A = [ row[:n2] for row in M[:n2] ]
    B = [ row[n2:] for row in M[:n2] ]
    C = [ row[:n2] for row in M[n2:] ]
    D = [ row[n2:] for row in M[n2:] ]

    return [A, B, C, D]

# Merge 4 quadrants into a matrix
def merge_quadrants(*Q: list[list[list[int]]]) -> list[list[int]]:
    n = len(Q[0])

    return [ Q[0][i] + Q[1][i] for i in range(n) ] + [ Q[2][i] + Q[3][i] for i in range(n) ]

# Multiply two matrices using the recursive method
def matrix_mul_rec(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    n = len(A) # n is a power of 2

    if (n == 1):
        return [[A[0][0]*B[0][0]]]
    
    A, B = split_quadrants(A), split_quadrants(B)

    C = [0, 0, 0, 0]
    for i in range(2):
        for j in range(2):
            C[i*2+j] = matrix_sum(matrix_mul_rec(A[i*2], B[j]), matrix_mul_rec(A[i*2+1], B[2+j]))

    return merge_quadrants(*C)

# Multiply two matrices using the Strassen method
def matrix_mul_strassen(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    n = len(A) # n is a power of 2

    if (n == 1):
        return [[A[0][0]*B[0][0]]]

    A, B = split_quadrants(A), split_quadrants(B)

    A2 = [
        matrix_sum(A[1], matrix_neg(A[3])),
        matrix_sum(A[0], A[3]),
        matrix_sum(A[0], matrix_neg(A[2])),
        matrix_sum(A[0], A[1]),
        A[0],
        A[3],
        matrix_sum(A[2], A[3])
    ]

    B2 = [
        matrix_sum(B[2], B[3]),
        matrix_sum(B[0], B[3]),
        matrix_sum(B[0], B[1]),
        B[3],
        matrix_sum(B[1], matrix_neg(B[3])),
        matrix_sum(B[2], matrix_neg(B[0])),
        B[0]
    ]

    P = [ matrix_mul_strassen(A2[i], B2[i]) for i in range(7) ]

    return merge_quadrants(
        matrix_sum(P[0], P[1], matrix_neg(P[3]), P[5]),
        matrix_sum(P[3], P[4]),
        matrix_sum(P[5], P[6]),
        matrix_sum(P[1], matrix_neg(P[2]), P[4], matrix_neg(P[6]))
    )

print(matrix_mul_iter([[0,3,0,0],[0,0,5,0],[0,3,0,0],[0,0,5,0]], [[0,7,0,0],[11,0,0,0],[0,0,0,3],[0,0,5,0]]))
print(matrix_mul_rec([[0,3,0,0],[0,0,5,0],[0,3,0,0],[0,0,5,0]], [[0,7,0,0],[11,0,0,0],[0,0,0,3],[0,0,5,0]]))
print(matrix_mul_strassen([[0,3,0,0],[0,0,5,0],[0,3,0,0],[0,0,5,0]], [[0,7,0,0],[11,0,0,0],[0,0,0,3],[0,0,5,0]])) 