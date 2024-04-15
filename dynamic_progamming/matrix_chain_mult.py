def matrix_chain_mult(A: list[list[int]], B: list[list[int]]):
    if (len(A[0]) != len(B)):
        raise ValueError('Incompatible matrices')

    p = len(A)
    q = len(A[0])
    r = len(B[0])

    C = [[0]*r for _ in range(p)]

    for i in range(p):
        for j in range(r):
            C[i][j] = A[i][0]*B[0][j]
            for k in range(1, q):
                C[i][j] += A[i][k]*B[k][j]

    return C