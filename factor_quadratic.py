#!/usr/bin/env python3
"""factor_quadratic.py"""

from sympy import symbols, Eq, solve, sqrt
from sympy import symbols, Eq, solve, I
from numpy import arange
# arange imported from numpy to work with non integers




def factor_quadratic(h: float, i: float, j: float) -> None:
    """Displays factors of the quadratic polynomial Jx^2 + Kx + L"""

    print(f"Given the quadratic:{h}x^2 + {i}x + {j}")

    for a in arange(1, h + 1):
        if h % a == 0:
            c = h // a
            for b in arange(1, j + 1):
                if j % b == 0:
                    d = j // b
                    if a * d + b * c == i:
                        print(f"The factors are: ({a}x + {b})({c}x + {d})")
                    

# for factor_quadratic (h, i, j) for ax2 + bx + c
def main() -> None:
    h = 115425 
    i = 3254121
    j = 379021
            # answer is prime
# wolfram alpha says that there are no real solutions when j= 379021 
    # The extension field K of a field F is called 
    # a splitting field for the polynomial f(x) 
    # in F[x] if f(x) factors completely into linear factors 
    # in K[x] and f(x) does not factor
    # completely into linear factors over any proper subfield of K containing F
    #  (Dummit and Foote 1998, p. 448).
    # 
    
    factor_quadratic(h, i, j)


    #code modified from qis labs folder
    


if __name__ == "__main__":
    main()

def solve_equation():
    x = symbols('x')
    
    # Define the equation
    equation = Eq(115425 * x * x + 3254121 * x +379021, 0)

    
    # Solve the equation
    solutions = solve(equation, x)
    
    return
# this code is modified from ChatGPT, to find a solution if there are no factors 



# Example usage
solutions = solve_equation()
print(f"Solutions: {solutions}")
   
