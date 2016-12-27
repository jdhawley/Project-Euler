"""
Solution for problem 12 of Project Euler.

What is the value of the first triangle number to have over five hundred divisors?
"""


def solve():
    """
    Serves as the driver for problem 12.
    """
    def find_num_factors(top):
        """
        Finds the number of factors that any given number has.
        """
        num_factors = 0

        if top == 1:
            return 1

        for i in range(1, int(top ** .5) + 1):
            if top % i == 0:
                num_factors += 2
        return num_factors

    triangle_number = 1
    total = 0

    while True:
        total += triangle_number

        if find_num_factors(total) > 500:
            break

        triangle_number += 1

    return total


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nWhat is the value of the first triangle number to have over five hundred divisors?\n"
