from flask import Blueprint, render_template, session


bp_home = Blueprint(
    "Home",
    __name__,
    template_folder="templates",
)


@bp_home.route("/")
def index():

    if 'won_games' not in session:
        session['won_games'] = 0
    if 'lost_games' not in session:
        session['lost_games'] = 0

    return render_template("index.html")
