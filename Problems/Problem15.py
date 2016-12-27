"""
Solution for problem 15 of Project Euler.

How many lattice paths are there through a 20×20 grid?
"""


def solve():
    """
    Serves as the driver for problem 15.
    """
    board = [[0 for i in range(21)] for j in range(21)]

    for i in range(len(board) - 1):
        board[i][len(board) - 1] = 1
        board[len(board) - 1][i] = 1

    for i in range(len(board) - 1)[::-1]:
        for j in range(len(board) - 1)[::-1]:
            board[i][j] = board[i + 1][j] + board[i][j + 1]

    return board[0][0]


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nHow many lattice paths are there through a 20×20 grid?\n"
