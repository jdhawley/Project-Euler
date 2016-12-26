"""
Solution for problem 10 of Project Euler.

Find the sum of all the primes below two million.
"""


def solve():
    """
    Serves as the driver for problem 10.
    """
    def is_prime(num):
        """
        Performs a primality test on a number.
        """
        if num < 4:
            return True
        if num % 2 == 0:
            return False
        if num % 3 == 0:
            return num == 3
        k = 3
        while k * k <= num:
            if num % k == 0:
                return False
            k += 2
        return True

    primes = [1]
    sieve = [True] * 2000000
    for i in range(2, len(sieve)):
        if sieve[i]:
            if is_prime(sieve[i]):
                primes.append(i)
                sieve[i::i] = [False] * (1999999 // i)

    return sum(primes)


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nFind the sum of all the primes below two million.\n"
