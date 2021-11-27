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
        try:
            next_index = word.index(letter, index_position)
            if next_index not in indexes:
                indexes.append(next_index)
            index_position += 1
        except ValueError:
            break

    return indexes


def get_game_status():
    """ Return the current game status"""
    game_status = {
        # "word": session.get('guessing_word', None),
        "incorrect_guesses": session.get('incorrect_guesses', None),
        "game_state": session.get('game_state', None),
        "word_length": session.get('word_length', None),
        "guesses": session.get('guesses', None),
    }

    return game_status
