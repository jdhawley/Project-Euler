"""
Solution for problem 9 of Project Euler.

There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
"""
import math


def solve():
    """
    Serves as the driver for problem 9.
    """
    for a in range(1, 1001):
        for b in range(1, 1001):
            num = a * a + b * b
            c = int(math.sqrt(num))
            if a + b + c == 1000:
                if a * a + b * b == c * c:
                    return a * b * c


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nThere exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.\n"
