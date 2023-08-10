#!/usr/bin/env python3
"""werner_formula.py"""

import numpy as np
import matplotlib.pyplot as plt

a = .8
b = .5
"""define f(x)"""
def f1(x):
    return np.sin(a * x)

def f2(x):
    return np.sin(b * x)

def f3(x):
    return f1(x) * f2(x)

def f4(x): # werner formula
    return (1/2) * ((np.cos((a - b) * x)) - np.cos((a + b) * x))


"""set values"""
x = np.linspace(-3 * np.pi, 3 * np.pi, 500) # creates x values

y1 = f1(x) # creates y values
y2 = f2(x)
y3 = f3(x)
y4 = f4(x)


"""plot using LaTeX """
plt.plot(x, y1, label=r"$f_1(x) = \sin(0.8x)$")
plt.plot(x, y2, label=r"$f_2(x) = \sin(0.5x)$")
plt.plot(x, y3, label=r"$f_1(x) \cdot f_2(x)$")
plt.plot(x, y4, "r-.o", label=r"Werner's Product-to-Sum formula")
plt.legend() # adds legend


def main() -> None:
    plt.show() #show plot


if __name__ == "__main__":
    main()

# Attributions: 
    # https://en.wikipedia.org/wiki/Prosthaphaeresis
    # Werner's Product-to-Sum formula is defined as:
        #sin(𝑎) * sin(𝑏) = (1/2) * (cos(𝑎 - 𝑏) - cos(𝑎 + 𝑏))
    # ChatGPT used on July 5, 2023-- OpenAI, communication, July 5, 2023