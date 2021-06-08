"""Codewars Rectangle into Squares Kata"""
import math


def square_in_rectangles(length, width):
    """This function is the solution to the Codewars Rectangle into Squares Kata that
        can be found here https://www.codewars.com/kata/55466989aeecab5aac00003e/train/python."""

    if length == width:
        return None

    number_of_units = length * width
    potential_squares = []
    for number in reversed(range(1, number_of_units + 1)):
        int_square_root = int(math.sqrt(number))
        if number == int_square_root * int_square_root:
            potential_squares.append(int_square_root)

    units_left = number_of_units
    squares = []
    for potential_square in potential_squares:
        units_left = units_left - (potential_square * potential_square)
        if units_left > 0:
            squares.append(potential_square)
        elif units_left == 0:
            return squares
        elif units_left < 0:
            squares = []
            units_left = number_of_units

    min_square = min(potential_squares)
    while units_left > 0:
        units_left = units_left - (min_square * min_square)
        squares.append(min_square)

    return squares
