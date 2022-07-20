from katas.tennis_game_points import tennis_game_points


def test_tennis_game_points():
    assert tennis_game_points("15-40") == 4
    assert tennis_game_points("30-all") == 4
    assert tennis_game_points("love-15") == 1
    assert tennis_game_points("love-30") == 2
    assert tennis_game_points("love-40") == 3
    assert tennis_game_points("15-love") == 1
    assert tennis_game_points("15-30") == 3
