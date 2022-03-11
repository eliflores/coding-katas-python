"""Codewars Duplicate Encoder Kata"""


def duplicate_encode(word):
    """This function is the solution to the Codewars Duplicate Encoder Kata that
    can be found at:
    https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python."""

    word_lowercase = word.lower()
    occurrences = {}
    for character in list(word_lowercase):
        number_of_times = occurrences.get(character, 0)
        number_of_times += 1
        occurrences[character] = number_of_times

    encoded_string = []
    for character in word_lowercase:
        if occurrences[character] == 1:
            encoded_string.append('(')
        else:
            encoded_string.append(')')

    return ''.join(encoded_string)
