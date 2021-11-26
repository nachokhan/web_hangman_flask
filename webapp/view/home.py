from flask import Blueprint, render_template


bp_home = Blueprint(
    "Home",
    __name__,
    template_folder="templates",
)


@bp_home.route("/")
def index():
    return render_template("index.html")
