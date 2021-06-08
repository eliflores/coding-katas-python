from katas.rectangle_into_squares import square_in_rectangle


def test_square_in_rectangles():
    assert square_in_rectangle(5, 5) is None
    assert square_in_rectangle(5, 3) == [3, 2, 1, 1]
    assert square_in_rectangle(20, 14) == [14, 6, 6, 2, 2, 2]
    assert square_in_rectangle(37, 14) == [14, 14, 9, 5, 4, 1, 1, 1, 1]
