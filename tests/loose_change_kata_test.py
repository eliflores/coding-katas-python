from loose_change_kata import loose_change


def test_returns_all_coins_equal_to_0_when_given_an_amount_equal_to_0():
    assert loose_change(0) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}


def test_returns_all_coins_equal_to_0_when_given_a_negative_amount():
    assert loose_change(-435) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(-2) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}


def test_rounds_the_amount_down_when_the_given_amount_is_a_float():
    assert loose_change(4.935) == {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(3.9) == {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}


def test_loose_change_returns_the_least_amount_of_coins():
    assert loose_change(56) == {'Nickels': 1, 'Pennies': 1, 'Dimes': 0, 'Quarters': 2}
    assert loose_change(29) == {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}
    assert loose_change(91) == {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3}

