#!/usr/bin/env python3
"""random_walk_gamma.py"""

from matplotlib.axes import Axes

import numpy as np

import typing
import matplotlib.pyplot as plt
from scipy.special import gamma  # type: ignore

if typing.TYPE_CHECKING:
    from numpy.typing import NDArray


def plot(ax: Axes) -> None:
    n: int = 20_000 
    x: NDArray[np.float_] = np.linspace(1, 25, 100, dtype=np.float_)

    """calculating the expected mean value of the equation """
    # n is dimension 
    # gamma is euler's gamma function
    y: NDArray[np.float_] = np.sqrt(2 * n / x) * np.power(  # Euler's Gamma Function
        gamma((x + 1.0) / 2) / gamma(x / 2), 2  # type:ignore
    )

    """Define axes and line width"""
    ax.plot(x, y, linewidth=2)

    """ Axes Titles"""
    ax.set_title("Mean Final Distance of a \n Uniform Random Walk on a Unit Lattice ")
    ax.set_xlabel("Dimensions") # X axis
    ax.set_ylabel("Mean Final Distance") # y axis


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()

if __name__ == "__main__":
    main()

# Attributions: Code is from Dr. Biersach's QIS101 