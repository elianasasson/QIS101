#!/usr/bin/env python3
"""prime_racer4.py"""

from math import isqrt  # finds integer sqrt
from random import randint, seed
from time import process_time


def is_prime(n: int) -> bool:
    """Returns True/False if the given number is prime"""
    if n < 2:
        return False
    if n % 2 == 0: 
        return False
    if n % 3 == 0:
        return False
    # makes code faster to eliminate the smaller numbers, then can do larger spacing 
    for factor in range(5, isqrt(n) + 1, 6): 
        #  no need for 2 spacing at a time, 6 is good
        if n % factor == 0 or n % (factor + 2) == 0:
            # need both to prevent a / by 0 error
            return False
             # all other numbers will be prime
             #these three lines were optimized by chatgpt
    return True


def main() -> None:
    seed(2016)

    num_samples: int = 10_000
    min_val: int = 100_000
    max_val: int = 1_000_000

    print(
        (
            f"Counting the number of primes in {num_samples:,} random samples\n"
            f"with each sample having a value between {min_val:,} "
            f"and {max_val:,} inclusive . . ."
        )
    )

    samples: list[int] = [randint(min_val, max_val) for _ in range(num_samples)]

    start_time: float = process_time()
    num_primes: int = sum(is_prime(n) for n in samples)
    elapsed_time: float = process_time() - start_time

    print(f"Number of primes found: {num_primes:,}")
    print(f"Total run time (sec): {elapsed_time:.5f}\n")


if __name__ == "__main__":
    main()

# Total run time (sec): 0.01358
    # run time is varying from 0.010 to 0.019
        #normally around 0.014 - 0.015
#(base) eliana@Elianas-MacBook-Air labs % 

# modified code from prime racer 3