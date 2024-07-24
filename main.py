from flask import Flask
from flask_restful import Api

import api_git
import api_meropriation
from data import db_session
from flask_login import LoginManager

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

app.register_blueprint(api_git.blueprint)
app.register_blueprint(api_meropriation.blueprint)
db_sess = db_session.global_init('db/Dbase.db')


def main():
    app.run()


if __name__ == '__main__':
    app.run()
