class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []
        Player.all.append(self)

    def get_username(self):
        return self._username
    
    def set_username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception("raised an exception")
        
    username= property(get_username, set_username)
   
    def results(self, new_result=None):
        from classes.result import Result
        if isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results
        
    def games_played(self, new_game=None):
        from classes.game import Game
        if isinstance(new_game, Game):
            self._games_played.append(new_game)
        return self._games_played
    
    def played_game(self, game):
        return game in self._games_played

    def num_times_played(self, game):
        times_played = [g for g in self._games_played if game is g]
        return len(times_played)
    
    @classmethod
    def highest_scored(cls, game):
        pass
        
