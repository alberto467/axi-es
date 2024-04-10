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

def DFT(a: list[int]) -> list[complex]:
    n = len(a)
    c_root = cmath.exp(2*cmath.pi*1j/n)

    return [ sum([ a[j]*c_root**(k*j) for j in range(n) ]) for k in range(n) ]

# FFT

def FFT(a: list[int]) -> list[complex]:
    n = len(a)

    if (n == 1):
        return [ complex(a[0], 0) ]

    n2 = int(n/2)
    w_n = cmath.exp(2*cmath.pi*1j/n)
    w = complex(1, 0)

    y_even = FFT([ a[i] for i in range(0, n, 2) ])
    y_odd = FFT([ a[i] for i in range(1, n, 2) ])

    y = [0 for _ in range(n)]
    for k in range(n2):
        y[k] = y_even[k] + w*y_odd[k]
        y[k+n2] = y_even[k] - w*y_odd[k]
        w *= w_n

    return y

def build_vandermonde_matrix(n: int) -> np.ndarray[complex]:
    w_n = cmath.exp(2*cmath.pi*1j/n)

    mat = np.arange(n).reshape(n, 1)
    mat = mat*mat.T
    mat = np.power(w_n, mat)

    return mat

def FFT_matrix(a: list[int]) -> list[complex]:
    n = len(a)
    mat = build_vandermonde_matrix(n)
    return np.matmul(mat, np.array(a))

def inverse_FFT_matrix(a: list[complex]) -> list[int]:
    n = len(a)
    mat = build_vandermonde_matrix(n)
    mat = np.linalg.inv(mat)
    return np.matmul(mat, a)

def plot_FFT(data: np.ndarray):
    samples = len(data)
    nyquist_freq = int(samples/2)

    # Apply a Hanning window to the signal, to reduce spectral leakage
    window = np.hanning(samples)
    windowed_signal = data*window

    # Compute the FFT of the original and windowed signals
    fft = np.abs(FFT(data)[:nyquist_freq])
    windowed_fft = np.abs(FFT(windowed_signal)[:nyquist_freq])
    # Normalize the windowed FFT to have the same maximum as the original FFT, for viewing purposes
    windowed_fft = windowed_fft * (np.max(fft) / np.max(windowed_fft))
    
    # Plot the original and windowed signals, and their FFTs
    fig, (ax1, ax2) = plt.subplots(1, 2)

    ax1.set_title('Signal')
    ax1.plot(data, label='Original signal', color='blue')
    ax1.plot(window*np.max(data), label='Window', color='black', alpha=0.3)
    ax1.plot(windowed_signal, label='Windowed signal', color='red')
    ax1.legend()

    ax2.set_title('FFT')
    ax2.set_xscale('log')
    ax2.plot(fft, label='FFT', color='blue')
    ax2.plot(windowed_fft, label='Windowed FFT', color='red')
    ax2.legend()

    plt.show()

samples = 2**14
sines = np.sin(np.linspace(0, 2*np.pi*1000.7, samples)) + np.sin(np.linspace(0.3, 2*np.pi*47, samples))*0.7 + np.sin(np.linspace(0.1, 2*np.pi*4776.4, samples))*0.4
plot_FFT(sines)