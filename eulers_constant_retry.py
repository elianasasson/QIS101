#!/usr/bin/env python3
"""eulers_constant.py"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

""" define the integrand using Euler's constant formula """


def integrand(x):
    return -np.log(np.log(1 / x))


""" estimate Euler's constant """
gamma, _ = quad(integrand, 0, 1)  # scipy usage

""" change values to harmonic numbers """


def harmonic_number(n):
    return sum(1 / i for i in range(1, n + 1))  # i is throwaway variable


x = np.linspace(1, 51)
harmonic_numbers = [harmonic_number(n) for n in range(0, 50)]

""" plotting functions """
plt.step(x, harmonic_numbers, label="Harmonic Numbers")
plt.plot(
    x, gamma + np.log(np.log(x)), label="y + ln(ln(x))"
)  # superimposes on the same graph

plt.xlabel("n")
plt.ylabel("value")
plt.title("Euler's Constant and Harmonic Numbers")
plt.legend()
plt.grid()


def main() -> None:
    plt.show()


if __name__ == "__main__":
    main()

# Attributions: code help through codeacademy and chatgpt
