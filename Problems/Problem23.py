"""
Solution for problem 23 of Project Euler.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""


def solve():
    """
    Serves as the driver for problem 23.
    """

    def is_abundant(number):
        """
        Checks if a number is an abundant number.
        """

        abundant_sum = 1
        for j in range(2, int(number ** .5) + 1):
            if number % j == 0:
                if j == number // j:
                    abundant_sum += j
                else:
                    abundant_sum += j + (number // j)
        if abundant_sum > number:
            return True
        return False

    def fill_abundant(number, abundant_nums):
        """
        Creates a list of abundant numbers.
        """
        for j in range(number, 28123 + 1, number):
            if j not in abundant_nums:
                abundant_nums.append(j)
        abundant_nums.sort()

    def has_abundant_sum(number, abundant_nums):
        """Checks if a number has an abundant sum."""
        bottom_index, top_index = (0, 1)
        while abundant_nums[bottom_index] + abundant_nums[top_index] < number:
            top_index += 1

        while bottom_index <= top_index:
            if abundant_nums[bottom_index] + abundant_nums[top_index] == number:
                return True
            elif abundant_nums[bottom_index] + abundant_nums[top_index] > number:
                top_index -= 1
            else:
                bottom_index += 1
        return False

    abundant_numbers = []
    total = 0
    for i in range(1, 28123 + 1):
        if is_abundant(i):
            fill_abundant(i, abundant_numbers)

    for i in range(28123):
        if not has_abundant_sum(i, abundant_numbers):
            total += i

    return total


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nFind the sum of all the positive integers which cannot be written as the sum of two abundant numbers.\n"
