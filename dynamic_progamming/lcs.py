def LCS(x: str, y: str):
  m, n = len(x), len(y)

  # Tables of [0..m] x [0..n]
  l = [[0]*(n+1) for _ in range(m+1)]
  b = [[' ']*(n+1) for _ in range(m+1)]

  for i in range(1, m+1):
    for j in range(1, n+1):
      if (x[i-1] == y[j-1]):
        l[i][j] = 1 + l[i-1][j-1]
        b[i][j] = 'd'
      elif (l[i-1][j] >= l[i][j-1]):
        l[i][j] = l[i-1][j]
        b[i][j] = 'u'
      else:
        l[i][j] = l[i][j-1]
        b[i][j] = 'l'

  return l[m][n], b

def print_LCS(x, b, i, j):
  if (i == 0 or j == 0):
    return
  
  if (b[i][j] == 'd'):
    print_LCS(x, b, i-1, j-1)
    print(x[i-1], end='')
  elif (b[i][j] == 'l'):
    print_LCS(x, b, i, j-1)
  else:
    print_LCS(x, b, i-1, j)

def test_LCS():
  x = 'ciaocaro'
  y = 'caiaca'
  l, b = LCS(x, y)
  print(l)
  print_LCS(x, b, len(x), len(y))

test_LCS()