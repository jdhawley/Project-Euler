"""
Solution for problem 22 of Project Euler.

What is the total of all the name scores in Numbers22.txt?
"""
import os


def solve():
    """
    Serves as the driver for problem 22.
    """

    def find_score(name):
        """
        Returns the name score of a name.
        """
        score = 0
        for char in name:
            score += (ord(char) - 64)
        return score

    def get_data(fp):
        """
        Returns a list of names from the text file.
        """
        name_string = fp.read()

        name_list = name_string.split(",")
        for i in range(len(name_list)):
            name = name_list[i]
            name_list[i] = name[1:len(name) - 1]
        return name_list

    fn = os.path.join(os.path.dirname(__file__), '../Inputs/Numbers22.txt')
    f = open(fn, "r")
    names = sorted(get_data(f))
    total = 0
    for i in range(len(names)):
        total += find_score(names[i]) * (i+1)

    return total


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nWhat is the total of all the name scores in Numbers22.txt?\n"
