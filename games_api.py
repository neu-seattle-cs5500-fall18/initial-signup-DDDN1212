from db_operations import new_game, get_game, get_guesses, make_guess
from flask_restplus import Namespace, Resource, fields

api = Namespace('games')

game = api.model('Game', {
    'id': fields.Integer(),
    'word': fields.String(),
    'guesses': fields.List(fields.String),
    'correct_guesses': fields.List(fields.String),
    'max_guesses': fields.Integer(),
    'game_over': fields.Boolean(),
})

@api.route('/')
class Games(Resource):
    def post(self):
        """
        Creates a new game
        :return: ID of newly created game
        """
        return new_game()


@api.route('/<id>')
class Game(Resource):
    def get(self, id):
        """
        Gets the State of a specific game.
        :param id:
        :return: JSON of Game Object
        """
        return get_game(id)


@api.route('/<id>/guesses/<letter>')
class Guess(Resource):
    def post(self, id, letter):
        """
        Make a guess for a game
        :param id:
        :param letter:
        :return:
        """
        return make_guess(id, letter)


@api.route('/<id>/guesses')
class Guesses(Resource):
    def get(self, id):
        """
        Get history of guesses for a Game
        :param id:
        :return:
        """
        return get_guesses(id)
