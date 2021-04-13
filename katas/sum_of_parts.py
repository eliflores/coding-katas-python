"""Codewars Sums of Parts Kata"""


def parts_sums(numbers):
    """This function is the solution to the Codewars Loose Change Kata that
    can be found here https://www.codewars.com/kata/5ce399e0047a45001c853c2b/train/python."""
    ls_len = len(numbers)
    if ls_len == 0:
        return [0]

    sums = [sum(numbers)]
    for _ in range(ls_len):
        numbers.pop(0)
        sums.append(sum(numbers))

    return sums
