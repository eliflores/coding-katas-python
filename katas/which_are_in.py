"""Codewars Which are in? Kata"""


def in_array(array1, array2):
    """This function is the solution to the Codewars Which are in? Kata that
       can be found here https://www.codewars.com/kata/550554fd08b86f84fe000a58/train/python"""

    words_in_array = set()

    for word_from_array2 in array2:
        for word_from_array1 in array1:
            if word_from_array1 in word_from_array2:
                words_in_array.add(word_from_array1)

    return sorted(words_in_array)
