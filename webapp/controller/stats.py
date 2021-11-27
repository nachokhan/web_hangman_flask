from flask import session


def get_game_stats():
    """ Return the game statistics """
    game_stats = {
        "won": session.get('won_games', None),
        "lost": session.get('lost_games', None),
    }

    return game_stats
