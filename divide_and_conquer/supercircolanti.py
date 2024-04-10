def matrix_sum(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
  n = len(a)
  n2 = int(n/2)

  # Base case
  if (n == 1): return [[a[0][0]+b[0][0]]]
  
  # Divide
  a1 = [ r[:n2] for r in a[:n2] ]
  b1 = [ r[:n2] for r in b[:n2] ]
  a2 = [ r[n2:] for r in a[:n2] ]
  b2 = [ r[n2:] for r in b[:n2] ]

  # Recurse
  c1 = matrix_sum(a1, b1)
  c2 = matrix_sum(a2, b2)

  # Conquer
  return [ (c1[i] + c2[i]) for i in range(n2) ] + [ (c2[i] + c1[i]) for i in range(n2) ]

m1 = [[1,2],[2,1]]
m2 = [[3,4],[4,3]]

print(matrix_sum(m1, m2))

def matrix_scalar_mul(a: list[list[float]], b: float) -> list[list[float]]:
   return [ [ v*b for v in r ] for r in a ]

def matrix_mul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    n = len(a)
    n2 = int(n/2)

    # Base case
    if (n == 1): return [[a[0][0]*b[0][0]]]
    
    # Divide
    a1 = [ r[:n2] for r in a[:n2] ]
    b1 = [ r[:n2] for r in b[:n2] ]
    a2 = [ r[n2:] for r in a[:n2] ]
    b2 = [ r[n2:] for r in b[:n2] ]

    a_sum = matrix_sum(a1, a2)
    b_sum = matrix_sum(b1, b2)
    a_sub = matrix_sum(a1, matrix_scalar_mul(a2, -1))
    b_sub = matrix_sum(b1, matrix_scalar_mul(b2, -1))

    # Recurse
    u = matrix_mul(a_sum, b_sum)
    v = matrix_mul(a_sub, b_sub)

    # Conquer
    c1 = matrix_scalar_mul(matrix_sum(u, v), 1/2)
    c2 = matrix_scalar_mul(matrix_sum(u, matrix_scalar_mul(v, -1)), 1/2)
    return [ (c1[i] + c2[i]) for i in range(n2) ] + [ (c2[i] + c1[i]) for i in range(n2) ]

print(matrix_mul(m1, m2))