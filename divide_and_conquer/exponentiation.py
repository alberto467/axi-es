def power(x: float, n: int) -> float:
    # Base cases
    if (n == 0): return 1
    if (n == 1): return x
    # Divide
    k = int(n/2)
    # Recurse
    y = power(x, k)
    # Conquer
    if (n % 2 == 0): return y*y
    return y*y*x

def power_iter(x: float, n: int) -> float:
    if (n == 0): return 1

    p = 1
    s = x
    m = n

    while (m > 0):
        if (m % 2 == 1): p *= s
        s *= s
        m = int(m/2)

    return p

print(pow(3, 7), power(3, 7), power_iter(3, 7))
