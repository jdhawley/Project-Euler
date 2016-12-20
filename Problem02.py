"""
Solution for problem 2 of Project Euler.

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the
even-valued terms.
"""


def solve():
    """
    Serves as the driver for problem 2.
    """
    top = 4000000
    first, second, third = (0, 1, 0)
    total = 0
    while third < top:
        if third % 2 == 0:
            total += third
        first, second = (second, third)
        third = first + second
    return total


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nBy considering the terms in the Fibonacci sequence whose values do not exceed four million, find the " \
           "sum of the even-valued terms.\n"
