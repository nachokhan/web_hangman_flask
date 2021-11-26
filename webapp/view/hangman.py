from flask import Blueprint
from flask import session

import webapp.controller.hangman as hangman_controller


bp_hangman = Blueprint("Hangman", __name__)


def get_game_status():
    game_status = {
        # "word": session['guessing_word'],
        "incorrect_guesses": session['incorrect_guesses'],
        "game_state": session['game_state'],
        "word_length": session['word_length'],
        "guesses": session['guesses'],
    }

    return game_status


def get_game_stats():
    game_stats = {
        "won": session['won_games'],
        "lost": session['lost_games']
    }

    return game_stats


@bp_hangman.route("/game/new", methods=['POST'])
def new_game():
    error = None

    session['guesses'] = {}
    session['guessing_word'] = hangman_controller.get_random_word()
    session['word_length'] = len(session['guessing_word'])
    session['remaining_letters'] = len(session['guessing_word'])
    session['incorrect_guesses'] = 0
    session['correct_letters'] = []
    session['incorrect_letters'] = []
    session['game_state'] = "in_progress"

    status = get_game_status()
    stats = get_game_stats()

    return {"status": status, "stats": stats,  "error": error}


@bp_hangman.route("/game/check-letter/<string:letter>", methods=['POST'])
def word_contains_letter(letter: str):

    error = None
    indexes = None

    letter = letter.lower()

    word = session.get("guessing_word")

    if not (letter >= 'a' and letter <= 'z'):
        error = "Should only compare against letters"

    if len(letter) > 1:
        error = "Should only compare against a single letter"

    if not word:
        error = "There is no word to check against!"

    if letter in session['correct_letters']:
        error = "That letter was already guessed!"

    if letter in session['incorrect_letters']:
        error = "That letter was already guessed! And it was indeed wrong!"

    if session['game_state'] != "in_progress":
        error = "The game already finished! Start a new game."

    if not error:
        indexes = hangman_controller.get_all_ocurrences(word, letter)

        if indexes:
            session['guesses'][letter] = indexes
            session['correct_letters'].append(letter)
            session['remaining_letters'] -= len(indexes)
            if session['remaining_letters'] <= 0:
                session['game_state'] = "won"
                session['won_games'] += 1
        else:
            session['incorrect_guesses'] += 1
            session['incorrect_letters'].append(letter)
            if session['incorrect_guesses'] >= 10:
                session['game_state'] = "lost"
                session['lost_games'] += 1

    status = get_game_status()
    stats = get_game_stats()

    return {"status": status, "stats": stats,  "error": error}
