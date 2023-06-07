from classes.player import Player
from classes.game import Game


class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        self.player.results(self)
        self.player.games_played(self.game)
        self.game.results(self)
        self.game.players(self.player) 

    def get_score(self):
        return self._score
    
    def set_score(self, score):
        if isinstance(score, int) and 1 <= score <= 5000:
            self._score = score
        else:
            raise Exception("raise Exception")
    
    def get_game(self):
        return self._game
    
    def set_game(self, game):
        if isinstance(game, Game):
            self._game = game
        else:
            raise Exception('raised an exception')
    
    def get_player(self):
        return self._player
    
    def set_player(self, player):
        if isinstance(player, Player):
            self._player = player
        else:
            raise Exception("raised an exception")

    score = property(get_score, set_score)
    game = property(get_game, set_game)
    player = property(get_player, set_player)

