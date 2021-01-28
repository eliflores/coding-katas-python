from loose_change_kata import loose_change


def test_loose_change():
    assert loose_change(56) == {'Nickels': 1, 'Pennies': 1, 'Dimes': 0, 'Quarters': 2}
    assert loose_change(-435) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(4.935) == {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 0}
