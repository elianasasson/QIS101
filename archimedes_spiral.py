#!/usr/bin/env python3
"""archimedes_spiral.py"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

"""defining spiral radius to equal theta"""
def spiral_radius(theta):
    return theta

"""calculate the radius at each integral"""
def arc_length_integral(theta):
    return np.sqrt(1 + spiral_radius(theta) ** 2) # spiral radius formula

"""integrate to find the arc length at angle"""
def arc_length(theta):
    length = quad(arc_length_integral, 0, theta) # quad is used to integrate
    return length

"""evaluate spiral radii for each angle"""
def plot_spiral():
    theta_values = np.linspace(0, 8 * np.pi, 1000) # np.linespace is similar to arrange but specifies number of samples
    radius_values = [spiral_radius(theta) for theta in theta_values]
    # arrays needed to plot 

    plt.plot(radius_values * np.cos(theta_values), radius_values * np.sin(theta_values))
        # set radius values cos for x axis values and sin for y axis
    plt.xlabel("x \nDomain: -7π - 8π")
    plt.ylabel("y")
    plt.title("Archimedes Spiral \n r = θ")
    plt.grid()
    plt.axis("equal") # required for proper aspect ratio 
    # Set the x-axis ticks in increments of π from -7π to +8π
    plt.xticks(np.arange(-7*np.pi, 9*np.pi, np.pi), [ '-7π', '-6π', '-5π', '-4π', '-3π', '-2π', '-π', '0', 'π', '2π', '3π', '4π', '5π', '6π', '7π', '8π'])
    plt.show()

# Plot spiral
def main() -> None:
    plot_spiral()

if __name__ == "__main__":
    main()

# Attributions: Wolfram MathWorld (data on Archimedes Spiral), and code help through codeacademy and chatgpt