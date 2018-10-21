from game_app import db


class Game(db.Model):
    game_id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String, nullable=False)
    guesses = db.relationship('Guesses', backref='Game', lazy=True)
    correct_guesses = db.Column(db.ARRAY(db.CHAR))
    max_guesses = db.Column(db.SmallInteger, nullable=False, default=5)
    game_over = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return '<Game %r>' % self.id

    class Guesses(db.Model):
        guesses_id = db.Column(db.Integer, primary_key=True)
        game_id = db.Column(db.Integer, db.ForeignKey('game.game_id'), nullable=False)
        guess = db.Column(db.String, nullable=False)

        def __repr__(self):
            return '<Guess ID %r>' % self.id

