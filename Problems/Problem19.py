"""
Solution for problem 19 of Project Euler.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
import datetime


def solve():
    """
    Serves as the driver for problem 19.
    """
    date = datetime.date(1901, 1, 1)
    single_day = datetime.timedelta(1, 0, 0, 0, 0, 0, 0)
    sunday_count = 0
    while date < datetime.date(2001, 1, 1):
        if date.weekday() == 6 and date.day == 1:
            sunday_count += 1

        date += single_day

    return sunday_count


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nHow many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to " \
           "31 Dec 2000)?\n"
