"""
VIEW: HOME
"""
from flask import Blueprint, render_template
from ..controller import stats as stats_controller

bp_home = Blueprint(
    "Home",
    __name__,
    template_folder="templates",
)


@bp_home.route("/")
def index():
    """
    TODO
    """
    stats_controller.reset_stats()

    return render_template("index.html")
