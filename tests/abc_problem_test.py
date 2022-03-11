from katas.abc_problem import can_make_word


def test_can_make_word():
    assert can_make_word("A") is True
    assert can_make_word("BARK") is True
    assert can_make_word("BOOK") is False
    assert can_make_word("TREAT") is True
    assert can_make_word("COMMON") is False
    assert can_make_word("SQUAD") is True
    assert can_make_word("CONFUSE") is True
    assert can_make_word("BOUGHT") is False
    assert can_make_word("CAB") is True
    assert can_make_word("CABBAGE") is True
