from katas.pyramid_of_numbers_kata import levels_content


def test_returns_an_list_string_when_zero_is_given_as_input():
    assert levels_content(0) == []


def test_returns_the_levels_of_a_pyramid_of_numbers():
    assert levels_content(1) == ['1']
    assert levels_content(2) == ['1', '1 2 1']
    assert levels_content(3) == ['1', '1 2 1', '1 2 3 2 1']
    assert levels_content(4) == ['1', '1 2 1', '1 2 3 2 1', '1 2 3 4 3 2 1']
    assert levels_content(5) == ['1', '1 2 1', '1 2 3 2 1', '1 2 3 4 3 2 1',
                                 '1 2 3 4 5 4 3 2 1']
