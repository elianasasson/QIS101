#!/usr/bin/env python3
"""benfords_law.py"""


import random
import matplotlib.pyplot as plt

"""calculating the msd"""


def calculate_msd(n):  # MSD is the most significant digit
    while n >= 10:  # n is variable name; number
        n //= 10
    return n


"""generating random numbers"""


def generate_rn(count):  # generate_rn is generate random numbers
    numbers = []  # evaluates the single item on the list
    for __ in range(count):  # __ is "dummy variable"
        n = random.randint(1, 1000000)  # set range of random numbers
        n = n**100  # raise to the 100th power
        numbers.append(n)  # ChatGPT says to use append to add to the end of the list
    return numbers


"""digit probabilities """


def calculate_digit_probabilities(numbers):
    digit_counts = [0] * 10  # Initialize digit counts with zeros
    for n in numbers:
        msd = calculate_msd(n)  # msd is the result of the calculations
        digit_counts[msd] += 1

    digit_probabilities = [count / len(numbers) for count in digit_counts[1:]]
    return digit_probabilities


" Histogram Plotting"


def plot(probabilities):  # plot histogram
    digits = range(1, 10)
    plt.bar(digits, probabilities)
    plt.xlabel("Digit")
    plt.ylabel("Probability")
    plt.title("Benford's Law")
    plt.show()  # use plot show and not print for matplotlib


# generating random numbers
random_numbers = generate_rn(100000)

# probability of the msd
digit_probabilities = calculate_digit_probabilities(random_numbers)


# plotting histogram
def main() -> None:
    plot(digit_probabilities)


if __name__ == "__main__":
    main()

# help from ChatGPT, particularity with the the digit probabilities line
# code is slow, but may be my computer
