from flask import Flask
from app_config import APP_SECRET_KEY

from webapp.view.home import bp_home
from webapp.view.hangman import bp_hangman


app = Flask(__name__)
app.config['SECRET_KEY'] = APP_SECRET_KEY

app.register_blueprint(bp_home)
app.register_blueprint(bp_hangman)