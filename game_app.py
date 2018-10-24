
from flask import Flask
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ukswznuadkqpzj:9911370f41164cccbf9c917113d78b8dda8602cde1e15f02ce442fea175a4f8a@ec2-54-243-187-30.compute-1.amazonaws.com:5432/d7mep19ockkpfd'
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
