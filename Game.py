from game_app import db


class Game(db.model):
    game_id = db.column(db.Integer, primary_key=True)
    word = db.column(db.String, nullable=False)
    guesses = db.relationship('Guesses', backref='Game', lazy=True)
    correct_guesses = db.column(db.ARRAY(db.CHAR))
    max_guesses = db.column(db.SmallInteger, nullable=False, default=5)
    game_over = db.column(db.Boolean, nullable=False, default=False)

    class Guesses(db.model):
        id = db.Column(db.Integer, primary_key=True)
        game_id = db.Column(db.Integer, db.ForeignKey('game.game_id'), nullable=False)
        guess = db.Column(db.String, nullable=False)
