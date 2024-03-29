from katas.rectangle_into_squares import squares_in_rectangle


def test_square_in_rectangles_when_length_and_width_are_equal():
    assert squares_in_rectangle(5, 5) is None


def test_square_in_rectangles():
    assert squares_in_rectangle(5, 3) == [3, 2, 1, 1]
    assert squares_in_rectangle(20, 14) == [14, 6, 6, 2, 2, 2]
    assert squares_in_rectangle(37, 14) == [14, 14, 9, 5, 4, 1, 1, 1, 1]
