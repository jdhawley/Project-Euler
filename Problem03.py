"""
Solution for problem 3 of Project Euler.

What is the largest prime factor of the number 600851475143?
"""


def solve():
    """
    Serves as the driver for problem 3.
    """
    n = 600851475143
    last_factor, current_factor = (1, 2)
    while n > 1:
        if n % current_factor == 0:
            last_factor = current_factor
            while n % current_factor == 0:
                n /= current_factor
        current_factor += 1
    return last_factor


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nWhat is the largest prime factor of the number 600851475143?\n"
