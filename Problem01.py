"""
Solution for problem 1 of Project Euler.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
from sys import argv


def get_sum(top):
    """
    Mathematically efficient summation process.

    Computes the sum of numbers less than 1000 that are divisible by 3 or 5
    and subtracts the sum of numbers less than 1000 that are divisible by 15.
    """
    def sum_divisible_by(n):
        """Helper function created for stuff"""
        p = top // n
        return (n*(p*(p+1))) // 2
    return sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15)


def solve(top=1000):
    """
    Serves as the driver for problem 1.
    """
    top = int(argv[1])
    print(get_sum(top-1))   # Takes 00.000 seconds for 100,000,000


def display_problem():
    return "\nFind the sum of all multiples of 3 or 5 below any number (default size is 1000).\n"