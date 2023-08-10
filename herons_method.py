#!/usr/bin/env python3
"""herons_method.py"""

import random
# this allows for the random number generator to be used

def main() -> None:
    def herons_method(s, e):
        r = random.uniform(1, s)  
            # random guesses for r
        while abs(r * r - s) > e:
            # need to use absolute value of the numbers 
            # e is short for epsilon 
            r = (r + s / r) / 2
        return r
        # Generate random integer s between 10^6 and 2*10^6
    s = random.randint(10**6, 2 * 10**6)

    # Set epsilon to 10^(-8)
    e = 10 ** (-8)
    # Estimate square root using Heron's Method
    r = herons_method(s, e)

# Display s and r rounded to eight decimal places
    print(f"s = {s}")
    print(f"r = {r:.8f}")

if __name__ == "__main__":
    main()

#  chatgpt for the abs()  and random.uniform 
# random.uniform() is used to return a random num
    # chatgpt helped with def and usage





