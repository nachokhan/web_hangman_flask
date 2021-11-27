from flask import session


def reset_stats():
    if 'won_games' not in session:
        session['won_games'] = 0
    if 'lost_games' not in session:
        session['lost_games'] = 0


def get_stats():
    """ Return the game statistics """

    games_won = session.get('won_games', None)
    games_lost = session.get('lost_games', None)

    game_stats = {
        "won": games_won,
        "lost": games_lost,
    }

    return game_stats
