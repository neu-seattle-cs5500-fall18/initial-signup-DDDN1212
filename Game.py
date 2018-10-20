from game_app import db


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String)
    guesses = db.relationship('Guesses', backref='Game', lazy=True)
    correct_guesses = db.Column(db.ARRAY(db.CHAR))
    max_guesses = db.Column(db.SmallInteger)
    game_over = db.Column(db.Boolean)

    def __repr__(self):
        return '<Game %r>' % self.id

    class Guesses(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
        guess = db.Column(db.String, nullable=False)

        def __repr__(self):
            return '<Guess ID %r>' % self.id

