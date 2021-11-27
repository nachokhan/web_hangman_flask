from os import MFD_HUGE_SHIFT
from flask import Blueprint

import webapp.controller.stats as stats_controller


bp_stats = Blueprint("Statistics", __name__)


@bp_stats.route("/game/stats/", methods=['GET'])
def get_stats():
    return stats_controller.get_stats()


@bp_stats.route("/game/stats/reset", methods=['POST'])
def reset_stats():
    stats_controller.reset_stats()
    return stats_controller.get_stats()