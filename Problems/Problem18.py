"""
Solution for problem 18 of Project Euler.

Find the maximum total from top to bottom of the triangle in Numbers18.txt.
"""
import os


def solve():
    """
    Serves as the driver for problem 18.
    """
    triangle = []
    fn = os.path.join(os.path.dirname(__file__), '../Inputs/Numbers18.txt')
    f = open(fn, "r")
    for line in f:
        triangle.append(list(map(int, line.split(" "))))
    f.close()

    for row in range(len(triangle) - 1)[::-1]:
        for col in range(len(triangle[row])):
            if triangle[row + 1][col] >= triangle[row + 1][col + 1]:
                triangle[row][col] += triangle[row + 1][col]
            else:
                triangle[row][col] += triangle[row + 1][col + 1]
    return triangle[0][0]

    return find_max(triangle)


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nFind the maximum total from top to bottom of the triangle in Numbers18.txt.\n"
