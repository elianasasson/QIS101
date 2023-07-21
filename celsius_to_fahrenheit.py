#!/usr/bin/env python3
"""celsius_to_fahrenheit.py"""
# lines modified from qis101 fahrenheit to celsius program


def main() -> None:
    for celsius in range(-44, 107, 4):
        fahrenheit: float = celsius * 9 / 5 + 32
        print(f"{celsius: >.2f} C = {fahrenheit: >.2f} F")

    celsius = 106
        # line above from ChatGPT
    fahrenheit: float = celsius * 9 / 5 + 32
    print(f" {celsius: >.2f} C = {fahrenheit: >.2f} F")


if __name__ == "__main__":
    main()


