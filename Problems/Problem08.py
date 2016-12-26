"""
Solution for problem 8 of Project Euler.

Find the thirteen adjacent digits in numbers08.txt that have the greatest product. What is the value of this product?
"""
import os


def solve():
    """
    Serves as the driver for problem 8.
    """
    def read_numbers():
        """
        Reads the numbers from Numbers08.txt and returns them in a list that the rest of the program can process.
        """
        fn = os.path.join(os.path.dirname(__file__), '../Inputs/Numbers08.txt')
        f = open(fn, "r")
        raw_input = f.read()
        number_list = []

        for char in raw_input:
            if char.isdigit():
                number_list.append(int(char))

        return number_list

    def product(start_index):
        """
        Finds the product of 13 elements in a list starting at start_index.
        """
        total = 1
        for num in numbers[start_index: start_index+13:]:
            total *= num
        return total

    numbers = read_numbers()
    largest = 0
    for i in range(1000-13):
        if product(i) > largest:
            largest = product(i)
    return largest


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nFind the thirteen adjacent digits in numbers08.txt that have the greatest product. What is the value of" \
           "this product?\n"
