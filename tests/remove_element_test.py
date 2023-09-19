from katas.remove_element import remove_element


def test_remove_element():
    list1 = [3, 2, 2, 3]
    assert remove_element(list1, 3) == 2
    assert list1 == [2, 2]

    list2 = [0, 1, 2, 2, 3, 0, 4, 2]
    assert remove_element(list2, 2) == 5
    assert list2 == [0, 1, 3, 0, 4]
