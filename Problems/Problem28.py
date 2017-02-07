"""
Solution for problem 28 of Project Euler.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral?
"""


def solve():
    """
    Serves as the driver for problem 28.
    """
    total = 1
    for i in range(2, 502):
        total += (4 * (i * i)) - (10 * i) + 7
        total += (4 * (i * i)) - (8 * i) + 5
        total += (4 * (i * i)) - (6 * i) + 3
        total += (4 * (i * i)) - (4 * i) + 1
    return total


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nWhat is the sum of the numbers on the diagonals in a 1001 by 1001 spiral?\n"
