from flask import Flask
from app_config import APP_SECRET_KEY

from webapp.view.home import bp_home


app = Flask(__name__)
app.config['SECRET_KEY'] = APP_SECRET_KEY

app.register_blueprint(bp_home)