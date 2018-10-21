from db_operations import new_game, get_game, get_guesses, make_guess
from flask_restplus import Namespace, Resource, fields

api = Namespace('games')

game = api.model('Game', {
    'game_id': fields.Integer(),
    'guesses': fields.List(fields.String),
    'correct_guesses': fields.List(fields.String),
    'max_guesses': fields.Integer(),
    'game_over': fields.Boolean(),
})


@api.response(400, 'Validation Error')
@api.route('/start')
class Games(Resource):
    @api.response(200, 'Success')
    def get(self):
        """
        Landing for a new game.
        :return:
        """
        return "Start a game"

    @api.response(201, 'Created New Game.')
    @api.marshal_with(game, code=201)
    def post(self):
        """
        Creates a new Game
        :return: ID of newly created resource
        """
        return new_game()


@api.route('/<game_id>')
@api.doc(params={'game_id': 'Record for an instance of a game.'})
class Game(Resource):
    @api.response(404, 'Cannot find game. If you entered id manually please check and try again.')
    @api.response(200, 'Got game.')
    @api.marshal_with(game, code=200)
    def get(self, game_id):
        """
        Gets the State of a specific game.
        :param game_id:
        :return: JSON of Game Object
        """
        return "Got State"
        #get_game(id)


@api.route('/games/<game_id>/guesses/<letter>')
@api.doc(params={'game_id': 'Record for an instance of a game.', 'letter': 'Letter user guessed'})
class Guess(Resource):
    @api.response(404, 'Cannot find game.  If you entered id manually please check and try again. ')
    @api.response(201, 'Created Guess.')
    @api.marshal_with(game, code=201)
    def post(self):
        """
        Create a guess.
        :return: game.
        """
        return "Posted guess"


@api.route('/<game_id>/guesses')
@api.doc(params={'game_id': 'Record for an instance of a game.'})
class Guesses(Resource):
    @api.response(404, 'Cannot find game.  If you entered id manually please check and try again. ')
    @api.response(200, 'Got Guesses for game id')
    def get(self, game_id):
        """
        Get history of guesses for a Game
        :param id:
        :return:
        """
        return "Got Guesses"
            #get_guesses(id)
