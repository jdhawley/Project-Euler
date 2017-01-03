"""
Solution for problem 24 of Project Euler.

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
from math import factorial


def solve():
    """
    Serves as the driver for problem 24.
    """
    def permeation(num_array, permutation_number):
        """
        Returns the lexicographic permutation at a specific index.
        """
        final_permutation = ""
        for j in reversed(range(0, len(num_array))):
            value = factorial(j)
            final_permutation += str(num_array.pop(permutation_number // value))
            permutation_number %= value
        return final_permutation

    number_array = []
    for i in range(10):
        number_array.append(str(i))

    return permeation(number_array, 999999)


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nWhat is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?\n"
