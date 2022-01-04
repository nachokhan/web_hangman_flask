"""
TODO
"""

from flask import session


def reset_stats():
    """
    TODO
    """
    if 'won_games' not in session:
        session['won_games'] = 0
    if 'lost_games' not in session:
        session['lost_games'] = 0


def get_stats():
    """ Return the game statistics """

    ratio_won = None
    games_won = session.get('won_games', None)
    games_lost = session.get('lost_games', None)
    if (games_won+games_lost) != 0:
        ratio_won = games_won / (games_won+games_lost)

    game_stats = {
        "won": games_won,
        "lost": games_lost,
        "ratio_won": ratio_won,
    }

    return game_stats
