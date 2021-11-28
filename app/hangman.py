from flask import Flask
from config import APP_SECRET_KEY

from view.home import bp_home
from view.hangman import bp_hangman
from view.stats import bp_stats


app = Flask(__name__)
app.config['SECRET_KEY'] = APP_SECRET_KEY

app.register_blueprint(bp_home)
app.register_blueprint(bp_hangman)
app.register_blueprint(bp_stats)
