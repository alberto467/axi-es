import numpy as np

# def dna_alignment():


COST_TABLE = {
    'A': { 'A': 1, 'C': -3, 'G': -3, 'T': -3 },
    'C': { 'A': -3, 'C': 1, 'G': -3, 'T': -3 },
    'G': { 'A': -3, 'C': -3, 'G': 1, 'T': -3 },
    'T': { 'A': -3, 'C': -3, 'G': -3, 'T': 1 }
}

def get_pair_cost(x: chr, y: chr, S: dict[chr, dict[chr, int]], g: int) -> int:
    if (x == '-' or y == '-'):
        return g
    
    return S[x][y]

def alignment_cost_exp(X: str, Y: str, S: dict[chr, dict[chr, int]], g: int):
    m, n = len(X), len(Y)

    if (n > m):
        raise ValueError('Length of X must be equal or superior to the length of Y')
    
    C = np.ndarray((m+1, n+1), dtype=int)

    # Inizializza la prima riga
    for j in range(n+1):
        C[0,j] = j*g

    for i in range(1, m+1):
        C[i,0] = i*g
        for j in range(1, n+1):
            no_gap = C[i-1,j-1] + get_pair_cost(X[i-1], Y[j-1], S, g)
            gap_x = C[i-1,j] + g
            gap_y = C[i,j-1] + g

            if no_gap >= gap_x and no_gap >= gap_y:
                C[i,j] = no_gap
            elif gap_x >= gap_y:
                C[i,j] = gap_x
            else:
                C[i,j] = gap_y

    return C

def alignment_cost(X: str, Y: str, S: dict[chr, dict[chr, int]], g: int):
    m, n = len(X), len(Y)

    if (n > m):
        raise ValueError('Length of X must be equal or superior to the length of Y')

    C = [ j*g for j in range(n+1) ]

    for i in range(1, m+1):
        x = X[i-1]
        prev = C[0]
        C[0] = i*g
        for j in range(1, n+1):
            y = Y[j-1]
            new = max(prev + get_pair_cost(x, y, S, g), C[j] + g, C[j-1] + g)
            prev = C[j]
            C[j] = new

    return C[n]

C = alignment_cost_exp('AGTT', 'ATT', COST_TABLE, -2)
print(C)

def align_strings(X: str, Y: str, C: np.ndarray, sep: chr):
    out_x, out_y = list(X), list(Y)

    m, n = C.shape
    m -= 1
    n -= 1

    while (m >= 0 and n >= 0):
      no_gap = C[m-1,n-1]
      gap_x = C[m-1,n]
      gap_y = C[m,n-1]

      if (no_gap >= gap_x and no_gap >= gap_y):
        m -= 1
        n -= 1
      elif (gap_x >= gap_y):
        out_y.insert(n, sep)
        m -= 1
      else:
        out_x.insert(m, sep)
        n -= 1

    return ''.join(out_x), ''.join(out_y)

print(align_strings('AGTT', 'ATT', C, '-'))