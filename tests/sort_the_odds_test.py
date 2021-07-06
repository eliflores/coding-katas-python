from katas.sort_the_odds import sort_array


def test_sort_the_ods():
    assert sort_array([]) == []
    assert sort_array([7, 1]) == [1, 7]
    assert sort_array([5, 3, 1, 8, 0]) == [1, 3, 5, 8, 0]
    assert sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
    assert sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
