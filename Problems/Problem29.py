"""
Solution for problem 29 of Project Euler.

How many distinct terms are in the sequence generated by a^b for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
"""


def solve():
    """
    Serves as the driver for problem 29.
    """
    distinct_numbers = set()
    for a in range(2, 101):
        currentNumber = a
        for b in range(99):
            currentNumber *= a
            distinct_numbers.add(currentNumber)
    return len(distinct_numbers)


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nHow many distinct terms are in the sequence generated by a^b for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?\n"