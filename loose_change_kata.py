import math


# Ref: https://www.codewars.com/kata/5571f712ddf00b54420000ee/train/python
def loose_change(cents):
    if cents <= 0:
        return {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    else:
        cents = math.floor(cents)
        quarters, mod_quarters = divmod(cents, 25)
        dimes, mod_dimes = divmod(mod_quarters, 10)
        nickels, mod_nickels = divmod(mod_dimes, 5)
        pennies = mod_nickels

        return {'Nickels': nickels, 'Pennies': pennies, 'Dimes': dimes, 'Quarters': quarters}
