#!/usr/bin/env python3
"""plot_trajectory.py"""


import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Load data from CSV file
data = []
with open("ray.csv") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip header (it has data names)
    for row in csvreader:
        data.append([float(row[0]), float(row[1])])

# Convert data to numpy arrays
data = np.array(data)

# Calculate time in nanoseconds
time = np.linspace(0, 0.1743, len(data))

# linear regression to find the line of best fit
slope, intercept, _, _, _ = stats.linregress(time, data[:, 1])
velocity = slope / 100.0  # Convert slope to velocity relative to c

# Calculate the height at which the particle was originally emitted
initial_height = data[0, 1] - intercept / 100.0  # Convert intercept to cm

# Convert height to kilometers
initial_height_km = initial_height / 100000.0

"""Plot settings"""
plt.plot(time, data[:, 1], "b.", label="Particle Path")
plt.plot(time, intercept + slope * time, "r-", label="Line of Best Fit")
plt.xlabel("Time (ns)")
plt.ylabel("Height (cm)")
plt.title("Particle Trajectory")
plt.legend()

def main() -> None:
    plt.show()
    print("Velocity (relative to c):", velocity)
    print("Initial height (km):", initial_height_km)


if __name__ == "__main__":
    main()

# Attributions:
# https://physics.okstate.edu/people/faculty-directory/93-pages/540-benton-rpl-studies-in-cosmic-ray-muons#:~:text=At%20sea%20level%2C%20the%20most,lifetime%20of%20approximately%202%20%C2%B5s.
# OpenAI, communication, July 10, 2023
# https://en.wikipedia.org/wiki/Cosmic_ray
# https://en.wikipedia.org/wiki/Particle_shower


