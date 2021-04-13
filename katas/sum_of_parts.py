"""Codewars Sums of Parts Kata"""


def parts_sums(ls):
    """This function is the solution to the Codewars Loose Change Kata that
    can be found here https://www.codewars.com/kata/5ce399e0047a45001c853c2b/train/python."""
    list_length = len(ls)
    if list_length == 0:
        return [0]

    last_sum = sum(ls)
    sums = [last_sum]
    for _ in range(list_length):
        last_sum = last_sum - ls.pop(0)
        sums.append(last_sum)

    return sums
