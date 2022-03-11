"""Codewars Sort the odd Kata"""


def sort_array(source_array):
    """This function is the solution to the Codewars Sort the odd Kata that
    can be found at:
    https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python."""

    odds = [n for n in source_array if n % 2 == 1]
    sorted_odds = sorted(odds)
    return [n if n % 2 == 0 else sorted_odds.pop(0) for n in source_array]
