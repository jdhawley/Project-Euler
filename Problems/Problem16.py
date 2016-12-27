"""
Solution for problem 16 of Project Euler.

What is the sum of the digits of the number 2^1000?
"""


def solve():
    """
    Serves as the driver for problem 16.
    """
    number = str(2 ** 1000)
    total = 0
    for num in number:
        total += int(num)
    return total


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nWhat is the sum of the digits of the number 2^1000?\n"
