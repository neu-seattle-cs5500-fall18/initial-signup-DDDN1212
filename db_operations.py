from Game import Game
from game_app import db


def get_all_games():
    games = Game.query.all()
    return games


def new_game():
    a_game = Game(word='Word', max_guesses=5, game_over=False, message="Make your first Guess")
    print(a_game.message, a_game.max_guesses, a_game.game_over, a_game.word)
    db.session.add(a_game)
    db.session.commit()

    return a_game


def get_game(record):
    a_game = Game.query(game_id=record)
    return a_game


def get_guesses(record):
    a_game = Game.query(game_id=record)
    guesses = a_game.guesses.query(a_game.game_id)
    return guesses


def make_guess(record, letter):
    a_game = Game.query(game_id=record)
    a_game.update_game(letter)
    a_game.guesses.session.add(a_game.game_id, letter)

    return a_game


def is_valid(letter):
    return len(letter) == 1 and letter.isalpha()
