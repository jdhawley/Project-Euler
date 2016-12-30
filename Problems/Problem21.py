"""
Solution for problem 21 of Project Euler.

Evaluate the sum of all the amicable numbers under 10000.
"""


def solve():
    """
    Serves as the driver for problem 21.
    """
    def sum_divisors(number):
        """
        Calculates the sum value of all whole divisors of a number.
        """
        divisor_sum = 1
        for i in range(2, int(number ** .5) + 1):
            if number % i == 0:
                divisor_sum += i
                divisor_sum += number // i
        return divisor_sum

    total = 0
    used_list = []
    for i in range(1, 10000):
        if i == sum_divisors(sum_divisors(i)) and i != sum_divisors(i):
            if i not in used_list:
                total += i
                total += sum_divisors(i)
                used_list.append(i)
                used_list.append(sum_divisors(i))

    return total


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nEvaluate the sum of all the amicable numbers under 10000.\n"
