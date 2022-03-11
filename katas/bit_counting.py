"""Codewars Bit Counting Kata"""


def count_bits(number):
    """This function is the solution to the Codewars Bit Counting that
    can be found at:
    https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python"""

    bits = []
    quotient = number

    while divmod(quotient, 2)[0] != 0:
        quotient, remainder = divmod(quotient, 2)
        bits.append(remainder)
    bits.append(quotient)

    return bits.count(1)
