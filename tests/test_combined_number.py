from katas.combined_number import combined_number


def test_combined_number():
    assert combined_number([1, 2, 3]) == "321"
    assert combined_number([50, 2, 1, 9]) == "95021"
    assert combined_number([5, 50, 56]) == "56550"
    assert combined_number([420, 42, 423]) == "42423420"
