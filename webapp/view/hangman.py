from flask import Blueprint

import webapp.controller.hangman as hangman_controller


bp_hangman = Blueprint("Hangman", __name__)

@bp_hangman.route("/word/random")
def get_random_word():    
    
    word = hangman_controller.get_random_word()

    return word

