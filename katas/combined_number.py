"""Combined Number Kata

From: https://cyber-dojo.org/creator/choose_ltf?exercise_name=Combined%20Number
"""

import itertools


def combined_number(numbers):
    """
    A function that accepts a list of non-negative integers, and returns their
    largest possible combined number as a string. For example:

    given [50, 2, 1, 9]  it returns "95021"    (9 + 50 + 2 + 1)
    given [5, 50, 56]    it returns "56550"    (56 + 5 + 50)
    given [420, 42, 423] it returns "42423420" (42 + 423 + 420)
    given [420, 42, 423] it returns "42423420" (42 + 423 + 420)

    Source [https://blog.svpino.com/about]
    """
    number_permutations = itertools.permutations(numbers)
    string_permutations = [
        "".join(str(number) for number in number_permutation)
        for number_permutation in number_permutations]

    biggest_number = max([int(n) for n in string_permutations])
    return str(biggest_number)
