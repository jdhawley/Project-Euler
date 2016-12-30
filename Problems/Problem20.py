"""
Solution for problem 20 of Project Euler.

Find the sum of the digits in the number 100!
"""


def solve():
    """
    Serves as the driver for problem 20.
    """
    factorial_value = 1
    for i in range(1, 101)[::-1]:
        factorial_value *= i

    total = 0
    while factorial_value > 1:
        total += factorial_value % 10
        factorial_value //= 10

    return total


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nFind the sum of the digits in the number 100!\n"
