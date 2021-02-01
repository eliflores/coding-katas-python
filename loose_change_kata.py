import math


# Ref: https://www.codewars.com/kata/5571f712ddf00b54420000ee/train/python
def loose_change(amount_in_cents):
    def calculate_coins():
        int_amount_in_cents = math.floor(amount_in_cents)
        quarters, mod_quarters = divmod(int_amount_in_cents, 25)
        dimes, mod_dimes = divmod(mod_quarters, 10)
        nickels, mod_nickels = divmod(mod_dimes, 5)
        pennies = mod_nickels

        return {'Nickels': nickels, 'Pennies': pennies, 'Dimes': dimes, 'Quarters': quarters}

    if amount_in_cents <= 0:
        return {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    else:
        return calculate_coins()
