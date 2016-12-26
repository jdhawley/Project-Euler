"""
Solution for problem 6 of Project Euler.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def solve():
    """
    Serves as the driver for problem 6.
    """
    sum_of_squares = 0
    for i in range(1, 101):
        sum_of_squares += i * i
    square_of_sum = sum(range(1, 101)) ** 2
    return square_of_sum - sum_of_squares


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nFind the difference between the sum of the squares of the first one hundred natural numbers and the " \
           "square of the sum.\n"
