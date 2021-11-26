import random
from enum import Enum


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
    word = random.choice(WORDS).lower()
    return word


def get_all_ocurrences(word, letter):
    """Returns all indexes of ocurrences"""
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
