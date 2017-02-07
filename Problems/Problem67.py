"""
Solution for problem 67 of Project Euler.

Find the maximum total from top to bottom in Numbers67.txt?
"""
import os


def solve():
    """
    Serves as the driver for problem 67.
    """
    triangle = []
    fn = os.path.join(os.path.dirname(__file__), '../Inputs/Numbers67.txt')
    f = open(fn, "r")
    for line in f:
        triangle.append(line.split(" "))
    f.close()
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            triangle[i][j] = int(triangle[i][j])

    for row in range(len(triangle) - 1)[::-1]:
        for col in range(len(triangle[row])):
            if triangle[row + 1][col] >= triangle[row + 1][col + 1]:
                triangle[row][col] += triangle[row + 1][col]
            else:
                triangle[row][col] += triangle[row + 1][col + 1]

    return triangle[0][0]


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nFind the maximum total from top to bottom in Numbers67.txt?\n"
