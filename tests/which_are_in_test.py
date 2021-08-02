from katas.which_are_in import in_array


def test_in_array():
    assert in_array(
        ["live", "arp", "strong"],
        ["lively", "alive", "harp", "sharp", "armstrong"]) == ['arp', 'live', 'strong']
    assert in_array(
        ["arp", "mice", "bull"],
        ["lively", "alive", "harp", "sharp", "armstrong"]) == ['arp']
    assert in_array(
        ["tarp", "mice", "bull"],
        ["lively", "alive", "harp", "sharp", "armstrong"]) == []
