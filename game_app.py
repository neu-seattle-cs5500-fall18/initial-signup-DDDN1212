from flask import Flask
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from games_api import api as games_ns

app = Flask(__name__)

api = Api(
    title='Hangman',
    version='1.0',
    description='An API for Hangman'
)

api.add_namespace(games_ns)
api.init_app(app)
db = SQLAlchemy(app)
db.create_all()


if __name__ == '__main__':
    app.run()
