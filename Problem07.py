"""
Solution for problem 7 of Project Euler.

What is the 10,001st prime number?
"""


def solve():
    """
    Serves as the driver for problem 7.
    """

    def isPrime(num):
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

    def findNext(num):
        while True:
            num += 2
            if isPrime(num):
                return num

    prime_number = 3
    for i in range(1, 10000):
        prime_number = findNext(prime_number)

    return prime_number


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nWhat is the 10,001st prime number?\n"
