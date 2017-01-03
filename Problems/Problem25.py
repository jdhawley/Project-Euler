"""
Solution for problem 25 of Project Euler.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""


def solve():
    """
    Serves as the driver for problem 25.
    """
    first, second, third, count = 0, 1, 0, 0
    while True:
        first, second, third = second, third, second+third
        count += 1
        if len(str(third)) == 1000:
            return count


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nWhat is the index of the first term in the Fibonacci sequence to contain 1000 digits?\n"
