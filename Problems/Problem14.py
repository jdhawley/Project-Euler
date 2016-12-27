"""
Solution for problem 14 of Project Euler.

Which starting number, under one million, produces the longest Collatz chain?
"""


def solve():
    """
    Serves as the driver for problem 14.
    """
    def get_chain_length(n):
        """Finds the length of a Collatz sequence for a given number."""
        if n in chain_lengths:
            return chain_lengths[n]
        else:
            if n == 1:
                chain_lengths[n] = 1
            elif n % 2 == 0:
                chain_lengths[n] = 1 + get_chain_length(n // 2)
            else:
                chain_lengths[n] = 1 + get_chain_length((3 * n) + 1)
        return chain_lengths[n]

    largest = 0
    number = 0
    chain_lengths = {}
    for i in range(1, 1000000):
        if largest < get_chain_length(i):
            largest = get_chain_length(i)
            number = i
    print(number)


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nWhich starting number, under one million, produces the longest Collatz chain?\n"
