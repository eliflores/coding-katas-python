"""Codewars Sums of Parts Kata"""


def validate(number):
    """This function is the solution to the Codewars Loose Change Kata that
    can be found at: https://www.codewars.com/kata/5418a1dd6d8216e18a0012b2/"""

    digits = [int(digit) for digit in str(number)]
    digits = every_other_digit_doubled(digits)
    digits = replace_digits_greater_than_9(digits)
    sum_of_all_digits = sum(digits)
    return sum_of_all_digits % 10 == 0


def every_other_digit_doubled(digits):
    doubled_digits = []

    for index, digit in enumerate(digits, start=1):
        if len(digits) % 2 == 0:
            if index % 2 == 1:
                doubled_digits.append(digit * 2)
            else:
                doubled_digits.append(digit)
        else:
            if index % 2 == 0:
                doubled_digits.append(digit * 2)
            else:
                doubled_digits.append(digit)

    return doubled_digits


def replace_digits_greater_than_9(digits_doubled):
    resulting_digits = []

    for digit in digits_doubled:
        if digit > 9:
            resulting_digits.append(digit - 9)
        else:
            resulting_digits.append(digit)

    return resulting_digits
