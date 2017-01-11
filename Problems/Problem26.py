"""
Solution for problem 26 of Project Euler.

Find the value of d < 1000 for which 1 / d contains the longest recurring cycle in its decimal fraction part.
"""


def solve():
    """
    Serves as the driver for problem 26.
    """
    def find_sequence_length(n):
        """Returns the length of the sequence provided by 1/n."""
        dividend = 1
        divisor = n
        past_remainders = []
        while True:
            remainder = dividend % divisor

            if remainder in past_remainders:
                return len(past_remainders) - past_remainders.index(remainder)

            if remainder == 0:
                return len(past_remainders) - 1

            past_remainders.append(remainder)
            dividend = remainder * 10

    max_length = 0
    max_index = 0
    for i in range(7, 1000, 2):
        if i % 3 == 0 or i % 5 == 0:
            continue
        length = find_sequence_length(i)
        if length > max_length:
            max_length = length
            max_index = i
    return max_index


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nFind the value of d < 1000 for which 1 / d contains the longest recurring cycle in its decimal" \
           "fraction part.\n"
