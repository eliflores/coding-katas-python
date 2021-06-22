from katas.validate_credit_card_number import validate


def test_validate_cc_number():
    assert validate(123) is False
    assert validate(1) is False
    assert validate(2121) is True
    assert validate(1230) is True
    assert validate(891) is False
