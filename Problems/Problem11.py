"""
Solution for problem 11 of Project Euler.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in
Numbers11.txt?
"""
import os


def solve():
    """
    Serves as the driver for problem 11.
    """
    fn = os.path.join(os.path.dirname(__file__), '../Inputs/Numbers11.txt')
    f = open(fn, "r")
    n = []
    largest = 0
    for line in f:
        n.append(line.split(" "))
    n = [list(map(int, x)) for x in n]

    for i in range(20):
        for j in range(20):
            if i > 2 and j < 17:            # Right upward diagonal
                number = n[i][j] * n[i - 1][j + 1] * n[i - 2][j + 2] * n[i - 3][j + 3]
                largest = max(largest, number)

            if j < 17:                      # Horizontal right
                number = n[i][j] * n[i][j + 1] * n[i][j + 2] * n[i][j + 3]
                largest = max(largest, number)

            if i < 17 and j < 17:           # Right downward diagonal
                number = n[i][j] * n[i + 1][j + 1] * n[i + 2][j + 2] * n[i + 3][j + 3]
                largest = max(largest, number)

            if i < 17:                      # Vertical downward
                number = n[i][j] * n[i + 1][j] * n[i + 2][j] * n[i + 3][j]
                largest = max(largest, number)

    return largest


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nWhat is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or " \
           "diagonally) in Numbers11.txt?\n"
