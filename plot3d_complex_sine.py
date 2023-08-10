#!/usr/bin/env python3
"""plot3d_complex_sine.py"""

import numpy as np
import matplotlib.pyplot as plt

# function definition
def f(z):
    return np.abs(np.sin(z))  # equation


# create complex grid
x = np.linspace(-2.5, 2.5)
y = np.linspace(-2.5j, 2.5j) # j is imaginary 
X, Y = np.meshgrid(x, y)
Z = f(X + Y)

# plot settings
fig = plt.figure()
ax = fig.add_subplot(projection="3d")  # set to 3d
ax.plot_surface(X.real, Y.imag, Z, cmap="tab20b")  # set colors, for smoother gradient set to 'magma'

# labels
ax.set_xlabel("Re(z)")  # x is real numbers
ax.set_ylabel("Im(z)")  # y is imaginary
ax.set_zlabel("|sin(z)|") # type: ignore

ax.set_title("Surface Plot of |sin(z)|")  # title


def main() -> None:
    plt.show()


if __name__ == "__main__":
    main()


# Atributions:
# https://www.geeksforgeeks.org/complex-numbers-in-python-set-1-introduction/
# OpenAI, communication, July 9, 2023
# https://matplotlib.org/stable/tutorials/colors/colormaps.html