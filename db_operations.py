from Game import Game
from game_app import db


def new_game():
    a_game = Game(word='Word')
    db.session.add(a_game)
    return a_game.game_id


def get_game(record):
    a_game = Game.query(game_id=record)
    return a_game


def get_guesses(record):
    a_game = Game.query(game_id=record)
    guesses = a_game.guesses.query(a_game.game_id)
    return guesses


def make_guess(record, letter):
    a_game = Game.query(game_id=record)
    guess_record = a_game.guesses.session.add(letter)
    return guess_record

