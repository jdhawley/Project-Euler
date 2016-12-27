"""
Solution for problem 17 of Project Euler.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
"""


def solve():
    """
    Serves as the driver for problem 17.
    """
    def count_chars(number):
        """
        Calculates the number of chars contained within the english version of an integer.
        """
        if number == 1000:
            return 11

        hundreds_place = number // 100
        number %= 100
        tens_place = number // 10
        number %= 10
        ones_place = number

        character_count = 0
        if hundreds_place != 0:
            character_count += word_lengths[hundreds_place] + 7
            if tens_place != 0 or ones_place != 0:
                character_count += 3

        if tens_place != 0:
            if tens_place == 1:
                if ones_place == 0:
                    character_count += tens[1]
                else:
                    character_count += word_lengths[10 + ones_place]
                return character_count
            else:
                character_count += tens[tens_place]

        if ones_place != 0:
            character_count += word_lengths[ones_place]

        return character_count

    word_lengths = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7,
                    17: 9, 18: 8, 19: 8}
    tens = {1: 3, 2: 6, 3: 6, 4: 5, 5: 5, 6: 5, 7: 7, 8: 6, 9: 6}
    total = 0

    for i in range(1, 1001):
        total += count_chars(i)

    return total


def display_problem():
    """
    Returns a string representing the problem being solved.
    """
    return "\nIf all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many " \
           "letters would be used?\n"
