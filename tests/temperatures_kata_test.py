from katas.temperatures_kata import temperature_closest_to_zero


def test_returns_the_only_temperature_when_only_one_is_provided():
    assert temperature_closest_to_zero([1]) == 1


def test_returns_zero_when_zero_is_given_in_the_temperatures():
    assert temperature_closest_to_zero([1, -2, -8, 4, -1, 0]) == 0


def test_returns_the_temperature_closest_to_zero():
    assert temperature_closest_to_zero([-20, -30, -25, -1, -2]) == -1
    assert temperature_closest_to_zero([1, -2, -8, 4, 5]) == 1
    assert temperature_closest_to_zero([1, -2, -8, 4, -1]) == 1
    assert temperature_closest_to_zero(
        [-5, -4, -2, 12, -40, 4, 2, 18, 11, 5]) == 2
