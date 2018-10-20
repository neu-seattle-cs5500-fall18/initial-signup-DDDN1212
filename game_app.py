from flask import Flask
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
db.create_all()

from games_api import api as games_ns

api = Api(
    title='Hangman',
    version='1.0',
    description='An API for Hangman'
)

api.add_namespace(games_ns)
api.init_app(app)

if __name__ == '__main__':
    app.run()
