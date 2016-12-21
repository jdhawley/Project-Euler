"""
Solution for problem 4 of Project Euler.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(regular_number):
    """
    Checks to see if a number is a palindrome.
    """
    def reverse(n):
        """
        Reverses a number for use in palindrome checking.
        """
        original_number = n
        reversed_number = 0
        while original_number > 0:
            reversed_number = (10 * reversed_number) + (original_number % 10)
            original_number //= 10
        return reversed_number

    return regular_number == reverse(regular_number)


def solve():
    """
    Serves as the driver for problem 4.
    """
    largest_palindrome = 0
    first = 999
    while first >= 100:
        second = 999
        while second >= first:
            if first * second <= largest_palindrome:
                break

            if is_palindrome(first * second):
                largest_palindrome = first * second

            second -= 1
        first -= 1

    return largest_palindrome


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nFind the largest palindrome made from the product of two 3-digit numbers.\n"
