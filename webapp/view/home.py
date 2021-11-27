from flask import Blueprint, render_template, session

import webapp.controller.stats as stats_controller

bp_home = Blueprint(
    "Home",
    __name__,
    template_folder="templates",
)


@bp_home.route("/")
def index():

    stats_controller.reset_stats()

    return render_template("index.html")
