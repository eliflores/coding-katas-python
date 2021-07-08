"""Codewars Sort the odd Kata"""


def sort_array(source_array):
    """This function is the solution to the Codewars Sort the odd Kata that
        can be found here https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python."""

    odds = list(filter(lambda n: n % 2 == 1, source_array))
    sorted_odds = sorted(odds)
    dest_array = []
    for number in source_array:
        if number % 2 == 0:
            dest_array.append(number)
        else:
            dest_array.append(sorted_odds.pop(0))

    return dest_array
