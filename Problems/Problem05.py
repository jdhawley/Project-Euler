"""
Solution for problem 5 of Project Euler.

What is the smallest number divisible by each of the numbers 1 to 20?
"""


def solve():
    """
    Serves as the driver for problem 5.
    """
    def isDivisible(number):
        for i in [11, 12, 13, 14, 15, 16, 17, 18, 19]:
            if number % i != 0:
                return False
        return True

    number = 20
    while True:
        if isDivisible(number):
            break
        number += 20

    return number


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nWhat is the smallest number divisible by each of the numbers 1 to 20?\n"
