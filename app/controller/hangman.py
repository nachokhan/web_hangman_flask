import random
from flask import session


WORDS = [
    "Camaraderie",
    "Blandishment",
    "Ebullient",
    "Grandiloquent",
    "Neophyte",
    "Maelstrom",
    "Torpid",
    "Anemone",
    "Worcestershire",
    "Redoubtable",
    "Ubiquitous",
    "otorrinolaringologo",
]


def get_random_word():
    """ Pick a random word from list/file/db/api """
    word = random.choice(WORDS).lower()
    return word


def get_all_ocurrences(word, letter):
    """Return a list of indexes of ocurrences of the letter
    in the word"""
    indexes = []

    index_position = 0
    while True:
        if letter == '':
            break
        try:
            next_index = word.index(letter, index_position)
            if next_index not in indexes:
                indexes.append(next_index)
            index_position += 1
        except ValueError:
            break

    return indexes


def update_game_status(ocurrences, letter):
    """Modify the status of the game by checking if there
    were ocurrences, how many and updating the game status
    according to the result.
    """
    if ocurrences:
        session['guesses'][letter] = ocurrences
        session['correct_letters'].append(letter)
        session['remaining_letters'] -= len(ocurrences)
        if session['remaining_letters'] <= 0:
            session['game_state'] = "won"
            session['won_games'] += 1
    else:
        session['incorrect_guesses'] += 1
        session['incorrect_letters'].append(letter)
        if session['incorrect_guesses'] >= 10:
            session['game_state'] = "lost"
            session['lost_games'] += 1


def check_letter(letter):
    """ Check if a letter is inside a word.
    After this call get_game_status() to get
    the new status of the game """

    word = session.get('word')
    indexes = get_all_ocurrences(word, letter)
    update_game_status(indexes, letter)


def init_new_game():
    """ Set all variables to init value and pick a random word"""

    session['guesses'] = {}
    session['word'] = get_random_word()
    session['word_length'] = len(session['word'])
    session['remaining_letters'] = len(session['word'])
    session['incorrect_guesses'] = 0
    session['correct_letters'] = []
    session['incorrect_letters'] = []
    session['game_state'] = "in_progress"


def get_game_status():
    """ Return the current game status"""
    game_status = {
        # "word": session.get('word', None),
        "incorrect_guesses": session.get('incorrect_guesses', None),
        "game_state": session.get('game_state', None),
        "word_length": session.get('word_length', None),
        "guesses": session.get('guesses', None),
    }

    return game_status


def is_valid_letter(letter):
    if not letter:
        return "There should be a letter there"
    if not (letter >= 'a' and letter <= 'z'):
        return "Should only compare against letters, not other characters."
    if len(letter) > 1:
        return "Should only compare against a single letter"


def letter_was_not_used(letter):
    if letter in session['correct_letters']:
        return "That letter was already guessed!"
    if letter in session['incorrect_letters']:
        return "That letter was already choosed! And it was indeed wrong!"


def is_valid_word():
    word = session.get("word")
    if not word:
        return "There is no word to check against!"


def is_game_in_progress():
    if 'game_state' not in session:
        return "If you don't start a new game there is no word to guess!"
    if session['game_state'] != "in_progress":
        return "The game already finished! Start a new game."
