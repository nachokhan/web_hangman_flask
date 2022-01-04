"""
VIEW: HANGMAN
"""
from flask import Blueprint
from ..controller import hangman as hangman_controller
from ..controller import stats as stats_controller


bp_hangman = Blueprint("Hangman", __name__)

@bp_hangman.route("/game/new", methods=['POST'])
def new_game():
    """
    TODO
    """
    hangman_controller.init_new_game()
    status = hangman_controller.get_game_status()
    return {"status": status}


@bp_hangman.route("/game/check-letter/<string:letter>", methods=['POST'])
def word_contains_letter(letter: str):
    """
    TODO
    """
    error = None

    letter = letter.lower()

    if not error:
        error = hangman_controller.is_game_in_progress()

    if not error:
        error = hangman_controller.is_valid_letter(letter)

    if not error:
        error = hangman_controller.is_valid_word()

    if not error:
        error = hangman_controller.letter_was_not_used(letter)

    if not error:
        hangman_controller.check_letter(letter)

    status = hangman_controller.get_game_status()

    return {"status": status, "error": error}


@bp_hangman.route("/game/status", methods=['GET'])
def get_status():
    """
    TODO
    """
    stats = stats_controller.get_stats()
    return {"stats": stats}
