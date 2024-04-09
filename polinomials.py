import cmath
import matplotlib.pyplot as plt
import numpy as np

# Evaluation: conversion from a list of coefficients to a list of values

def eval_polinomial_point(a: list[int], z: int) -> int:
    n = len(a)
    y = a[0]
    pow = 1
    for i in range(n-1):
        pow *= z
        y += a[i]*pow
    return y

def horner(a: list[int], z: int) -> int:
    n = len(a)
    y = a[n-1]
    for j in range(2, n+1):
        y = a[n-j] + z*y
    return y

def eval_polinomial(a: list[int], x: list[int]) -> list[int]:
    return [ horner(a, z) for z in x ]

# Interpolation: conversion from a list of values to a list of coefficients

# DFT

im_unit = complex(0,1)

def DFT(a: list[int]) -> list[complex]:
    n = len(a)
    c_root = cmath.exp(2*cmath.pi*im_unit/n)

    return [ sum([ a[j]*c_root**(k*j) for j in range(n) ]) for k in range(n) ]

# FFT

def FFT(a: list[int], n: int) -> list[complex]:
    if (n == 1):
        return [ complex(a[0], 0) ]

    n2 = int(n/2)
    w_n = cmath.exp(2*cmath.pi*im_unit/n)
    w = 1

    a_even = [ a[i] for i in range(0, n, 2) ]
    a_odd = [ a[i] for i in range(1, n, 2) ]
    y_even = FFT(a_even, n2)
    y_odd = FFT(a_odd, n2)

    y = [0 for _ in range(n)]
    for k in range(n2):
        y[k] = y_even[k] + w*y_odd[k]
        y[k+n2] = y_even[k] - w*y_odd[k]
        w *= w_n

    return y


sines = np.sin(np.linspace(0, 2*np.pi*512, 2**12)) + np.sin(np.linspace(0, 2*np.pi*47, 2**12))*0.7 + + np.sin(np.linspace(0, 2*np.pi*4776, 2**12))*0.4
sines_fft = FFT(sines, 2**12)

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.plot(sines)
ax2.plot([ abs(x) for x in sines_fft])
plt.show()