#!/usr/bin/env python3
"""maxwell_boltzmann.py"""

import numpy as np
import matplotlib.pyplot as plt

"""calculate the speed probability density functions"""
# formula is maxwell boltzmann distributions, showing speeds of particles in ideal gasses
def speed_pdf(s, t):
    # mb speed
    #t is temperature
    n = 4 * np.pi * (s**2) 
    # n is constant, s is speed
    exponential = np.exp(-s**2 / (2 * t))
    return n * exponential

def plot_pdfs(temperatures):
    speeds = np.linspace(0, 20) # domain 
    for t in temperatures:
        pdf = speed_pdf(speeds, t)
        plt.plot(speeds, pdf, label="{:.2f} Kelvin".format(t)) 
        # labels in the top right for the three lines, in default color

"""temperatures in Kelvin"""
temperatures = [1.0, 2.0, 5.0]

# Plot the PDFs of the Maxwell-Boltzmann distributions for different temperatures
plot_pdfs(temperatures)   
 
def main() -> None:
    plt.xlabel("Speed")
    plt.ylabel("Probability Density (PDF)")
    plt.title("Maxwell-Boltzmann Distribution")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()

# code is supplemented with help from ChatGPT