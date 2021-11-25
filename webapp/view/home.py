from flask import Blueprint


bp_home = Blueprint("Home", __name__)

@bp_home.route("/")
def index():
    return "Hola"


