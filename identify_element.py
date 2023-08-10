#!/usr/bin/env python3
"""identify_element.py"""


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sympy.solvers import solve


""" calculating molar mass of gas using ideal gas law"""

temp = np.array([-50, 0, 50, 100, 150])  # Temperature in Celsius
T = temp + 273.15  # Convert to Kelvin

L = np.array([11.6, 14.0, 16.2, 19.4, 21.8 ])  # Volume in liters
V = L / 1000  # Convert to m^3

# Ideal gas law PV = nRT
R = 0.0821  # R constant, atm⋅m^3/K⋅mol
P = 2.00 #atm
M = 50.00   #mass in grams 

def calculate_igl(n):
    n = (P * V * 1000) / (R * T) # multiply by 1000 as V is in m3 not L
    return n

# Calculate moles using the Ideal Gas Law
moles = calculate_igl(n=None)
print(f"Moles: {moles[0]}")

    # Calculate molar mass
def calc_molar(molar):
    molar = M / moles[0]  # Divide given mass (50g) by the number of moles (single value)
    return molar

molarmass = calc_molar(molar=None)
print(f"molar mass: {molarmass} g/mol")


""" Element/Compound ID"""

# Data dictionary to map molar mass to element
element_data = {
    4.0026: "Helium",
    12.0107: "Carbon",
    14.0067: "Nitrogen",
    15.9994: "Oxygen",
    18.9984: "Fluorine",
    39.948: "Argon, Ar"	,

# common compounds
    26.038: "Acetylene, C2H2",
    28.966: "Air",
    56.108: "1-Butene",	
    38.98: "sodium oxide",
    39.97: "potassium hydride",
    37.9968064: " fluorine, F2",
    38.01 : "Boron oxide",
# ions
    39.96: "Calcium ion (1+)",
    39.01: "HCNC radical anion",

    # Add more and their corresponding molar masses, as needed
}

# Identify the element based on molar mass
closest_mass = min(element_data, key=lambda x: abs(x - molarmass))
element_name = element_data.get(closest_mass, "Unknown Element")
print(f"The data provided indicates {element_name} is the closest approximation, at given temperature and pressure.")


""" graphing linear regression """

# Perform linear regression
slope, intercept, _, _, _ = stats.linregress(T, V)

# Generate interpolated data
T_interpolated = np.linspace(min(T), max(T), 100)
V_interpolated = intercept + slope * T_interpolated




def main() -> None:
     # Plot settings
    plt.plot(T, V, "ro", label="Data Points")
    plt.plot(T_interpolated, V_interpolated, "b-", label="Interpolated Curve")
    plt.xlabel("T (°K)")
    plt.ylabel("V (m^3)")
    plt.title("T vs. V Interpolated Curve")
    plt.legend()
    plt.grid()
    
    plt.show()

if __name__ == "__main__":
    main()



# This gas is closest to Argon, in terms of molecular weight, but it could also be a number of different compounds.


# Attributions
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html
# OpenAI, communication, July 10, 2023
# https://chem.libretexts.org/Courses/can/intro/11%3A_Gases/11.09%3A_The_Ideal_Gas_Law%3A_Pressure_Volume_Temperature_and_Moles
# https://webbook.nist.gov/chemistry/mw-ser/
    # database