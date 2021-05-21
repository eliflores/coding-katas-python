from katas.goat_latin import to_goat_latin


def test_to_goat_latin():
    assert to_goat_latin('I speak Goat Latin') == 'Imaa peaksmaaa oatGmaaaa atinLmaaaaa'
    assert to_goat_latin('The quick brown fox jumped over the lazy dog') == 'heTmaa uickqmaaa rownbmaaaa oxfmaaaaa ' \
                                                                            'umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa ' \
                                                                            'azylmaaaaaaaaa ogdmaaaaaaaaaa '
