from game_app import db


class Game(db.Model):
    game_id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String, nullable=False)
    guesses = db.relationship('Guesses', backref='Game', lazy=True)
    correct_guesses = db.Column(db.ARRAY(db.CHAR))
    incorrect_guesses = db.Column(db.Integer, nullable=False, default=0)
    max_guesses = db.Column(db.Integer, nullable=False, default=5)
    message = db.Column(db.String, nullable=False)
    game_over = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return '<Game %r>' % self.id

    class Guesses(db.Model):
        guesses_id = db.Column(db.Integer, primary_key=True)
        game_id = db.Column(db.Integer, db.ForeignKey('game.game_id'), nullable=False)
        guess = db.Column(db.CHAR, nullable=False)

        def __repr__(self):
            return '<Guess ID %r>' % self.id

    def update_incorrect_guesses(self, letter):
        """
        Method to increment incorrect guesses.
        :param letter: Letter guessed.
        :return: Void
        """
        if not self.word.__contains__(letter):
            self.incorrect_guesses += 1

    # Method to update State value of Game State dictionary.  Guessed Letter is placed in correct position in State.
    # Example: Guess l in Hello = **ll*
    def update_state(self, letter):
        """
        Method to update correct gueeses.  Guessed Letter is placed in correct position in State.
        Example: Guess l in Hello = **ll*
        :param letter:
        :return: Void
        """
        for index, element in enumerate(self.word):
            if element == letter:
                self.correct_guesses[index] = letter
            elif element.isalpha():
                self.correct_guesses[index] = element
            else:
                self.correct_guesses[index] = '*'

    def game_win(self):
        """
        Method to determine if User has won game.
        Where State = Word and User has not reached maximum guesses.
        :return: True if joined correct guesses equals word, false otherwise.
        """
        temp = ''.join(self.correct_guesses)
        return temp == self.word

    def game_lose(self):
        """
        Method to determine if user has lost.
        :return: True if incorrect guesses equals max guesses, false otherwise.
        """
        return self.incorrect_guesses == self.max_guesses

    def update_message(self, letter):
        """
         Method to determine correct message based on current game state
        :param letter:
        :return: String
        """
        if self.game_win(self):
            self.message = 'You have won'
        elif self.game_lose(self):
            self.message = 'You have lost'
        elif self.word.__contains__(letter):
            self.message = 'There is a %s' % letter
        else:
            self.message = 'There is no %s' % letter

    def update_game(self, letter):
        """
        Method to update the game based on user input.
        :param letter: Letter guessed.
        :return: Void.
        """
        self.update_incorrect_guesses(self, letter)
        self.update_state(self, letter)
        self.update_message(self, letter)
