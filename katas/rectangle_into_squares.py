"""Codewars Rectangle into Squares Kata"""
import math


def square_in_rectangle(length, width):
    """This function is the solution to the Codewars Rectangle into Squares Kata that
        can be found here https://www.codewars.com/kata/55466989aeecab5aac00003e/train/python."""

    if length == width:
        return None

    squares = []
    while length > 0 and width > 0:
        if width < length:
            max_square_size = width
            length = length - max_square_size
        else:
            max_square_size = length
            width = width - max_square_size
        squares.append(max_square_size)

    return squares
