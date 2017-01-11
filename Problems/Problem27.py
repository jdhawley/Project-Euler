"""
Solution for problem 27 of Project Euler.

Find the product of the coefficients for the quadratic expression that produces the maximum number of primes for
consecutive values of n.
"""


def solve():
    """
    Serves as the driver for problem 27.
    """
    def is_prime(n):
        if n < 1:
            return False
        if n % 2 == 0: return False
        if n % 3 == 0: return False
        for i in range(5, (n // 2) + 1, 2):
            if n % i == 0:
                return False
        return True

    def find_num_primes(a, b):
        """
        Computes the number of consecutive prime numbers.
        """
        n = 0
        while True:
            value = (n ** 2) + (a * n) + b
            if is_prime(value):
                n += 1
                continue
            return n

    def generate_primes():
        """
        Computes an infinite sequence of primes through the use of a generator implementation of the Sieve of
        Eratosthenes.

        Borrowed from the wonderful people at code.activestate.com/recipes/117119-sieve-of-eratosthenes/
        """
        D = {}
        q = 2
        while True:
            if q not in D:
                yield q
                D[q*q] = [q]
            else:
                for p in D[q]:
                    D.setdefault(p+q, []).append(p)
                del D[q]
            q += 1

    prime_generator = generate_primes()
    primes = set()
    while True:
        next_prime = next(prime_generator)
        if next_prime < 1000:
            primes.add(next_prime)
        else:
            break

    max_primes = 0
    max_product = 0
    for a in range(-999, 1000):
        for b in primes:
            num_primes = find_num_primes(a, b)
            if num_primes > max_primes:
                max_primes = num_primes
                max_product = a * b
    return max_product


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nFind the product of the coefficients for the quadratic expression that produces the maximum number of " \
           "primes for consecutive values of n.\n"
