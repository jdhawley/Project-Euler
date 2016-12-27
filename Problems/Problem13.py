"""
Solution for problem 13 of Project Euler.

Work out the first ten digits of the sum of the numbers in Numbers11.txt.
"""
import os


def solve():
    """
    Serves as the driver for problem 13.
    """
    fn = os.path.join(os.path.dirname(__file__), '../Inputs/Numbers13.txt')
    f = open(fn, "r")
    total = 0
    for line in f:
        total += int(line)
    return str(total)[:10:]


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nWork out the first ten digits of the sum of the numbers in Numbers11.txt.\n"
