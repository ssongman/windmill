from flask import Flask
from datetime import timedelta

app = Flask(__name__)

app.config.update(
    SECRET_KEY='F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT',
    SESSION_COOKIE_NAME='jpub_flask_session'
    PERMANENT_SESSION_LIFETIME=timedelta(31)
)