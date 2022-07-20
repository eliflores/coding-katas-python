"""Tennis Game Points Kata

From: https://www.codewars.com/kata/590942d4efde93886900185a

**Note**: Summer 2022 Kata Challenge - Kata 1.
"""

# A dictionary of corresponding call to number of points won
__TABLE_POINTS = {
    'love': 0,
    '15': 1,
    '30': 2,
    '40': 3
}


def tennis_game_points(score):
    """
    Returns an integer with the number of points won so far.

    Keyword arguments
    score -- A string in the format <p1>-<p2> representing a valid score,
    where <p1> is the first player's score, and <p2> is the second player's
    score.
    """

    p1, p2 = score.split('-')

    # when players are tied by one or two points, the score is described as
    # "15-all" and "30-all", respectively.
    if p2 == 'all':
        return __TABLE_POINTS.get(p1) * 2

    return __TABLE_POINTS.get(p1) + __TABLE_POINTS.get(p2)
