"""Codewars Rectangle into Squares Kata"""


def squares_in_rectangle(length, width):
    """This function is the solution to the Codewars Rectangle into Squares Kata
    that can be found at:
    https://www.codewars.com/kata/55466989aeecab5aac00003e/train/python."""

    if length == width:
        return None

    squares = []
    while length > 0 and width > 0:
        if width < length:
            squares.append(width)
            length = length - width
        else:
            squares.append(length)
            width = width - length

    return squares
