"""
Serves as a driver for the Project Euler Problems.

Provides a console interface for the user to view solutions
for any of the Project Euler problems I have solved thus far.
"""
import importlib
import os
import re
import sys


def get_solutions():
    """
    Returns a list of completed solutions.

    Scans the current directories for files matching the completed
    solution naming convention, and returns a list of all problem
    numbers with such a solution.
    """

    def is_solution(file_name):
        """Analyzes file name to determine if the file is a solution or not."""
        if solution_regex.match(file_name):
            return True
        return False

    def get_problem_number(file_name):
        """Returns the problem number from the file name."""
        problem_number = file_name[7: len(file_name) - 3]
        return problem_number

    solution_regex = re.compile("Problem\d+.py")
    solution_numbers = [get_problem_number(f) for f in os.listdir('.') if os.path.isfile(f) and is_solution(f)]

    return solution_numbers


def display_main_menu(completed_solutions):
    """
    Displays main menu for Project Euler Program.

    Allows the user to select a problem from the list of completed solutions,
    give input values to be solved, and run the solution.
    """
    print("Welcome to my Project Euler Solution Program!")
    print("Here are my completed problems:")
    for solution_number in completed_solutions:
        print("\t" + str(int(solution_number)))
    print("Additionally, you may enter 0 to quit.")

    try:
        problem_number = int(input("Please input the problem you would like to solve: "))
    except ValueError:
        print("Invalid input.")
        return display_main_menu(completed_solutions)

    if problem_number in map(int, completed_solutions):
        return problem_number
    elif problem_number == 0:
        sys.exit()
    else:
        return display_main_menu(completed_solutions)


def problem_confirmed():
    """
    Confirms that the selected problem is the intended problem.

    Displays a short menu and reads an input to ensure that the
    problem that was previously selected is the problem that was
    intended to be selected.
    """
    print("Is this the correct problem?")
    print("0: Exit")
    print("1: Yes")
    print("2: No")

    input_number = 0
    try:
        input_number = int(input("Please enter your answer here: "))
    except ValueError:
        problem_confirmed()

    if input_number == 0:
        sys.exit(0)
    elif input_number == 1:
        return True
    else:
        return False


def main():
    """
    Main function for the Project Euler Driver.

    Displays a menu with all completed solutions and in progress
    solutions, allowing the user to select a specific problem to
    solve.
    """
    completed_solutions = get_solutions()
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    print(os.path.dirname(os.path.abspath(__file__)))

    while True:
        problem_number = display_main_menu(completed_solutions)
        if problem_number < 10:
            file_name = "Problem0" + str(problem_number)
        else:
            file_name = "Problem" + str(problem_number)

        problem_module = importlib.import_module(file_name)
        print(problem_module.display_problem())
        if problem_confirmed():
            print("ANSWER: " + str(problem_module.solve()))


if __name__ == "__main__":
    main()
