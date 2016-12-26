"""
Solution for problem 7 of Project Euler.

What is the 10,001st prime number?
"""


def solve():
    """
    Serves as the driver for problem 7.
    """

    def is_prime(num):
        """
        Finds whether or not a number is prime.
        """
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        if num % 3 == 0:
            return False
        k = 3
        while k * k <= num:
            if num % k == 0:
                return False
            k += 2
        return True

    def find_next_prime(num):
        """
        Finds the next prime number after the number passed in.
        """
        while True:
            num += 2
            if is_prime(num):
                return num

    prime_number = 3
    for i in range(1, 10000):
        prime_number = find_next_prime(prime_number)

    return prime_number


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nWhat is the 10,001st prime number?\n"
