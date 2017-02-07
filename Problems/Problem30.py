"""
Solution for problem 30 of Project Euler.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""


def solve():
    """
    Serves as the driver for problem 30.
    """
    values = {}
    for i in range(10):
        values[i] = i**5

    successful_numbers = set()
    for i in range(2, 200000):
        number = i
        total = 0
        while number > 0:
            total += values[number % 10]
            number //= 10
        if i == total:
            successful_numbers.add(i)
    return sum(successful_numbers)


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nFind the sum of all the numbers that can be written as the sum of fifth powers of their digits.\n"
