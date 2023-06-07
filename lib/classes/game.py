class Game:
    def __init__(self, title):
        self.title = title
        self._results = []
        self._players = []
   
    def get_title(self):
        return self._title
    
    def set_title(self, title):
        if (not hasattr(self, "title")) and isinstance(title, str) and 0 < len(title):
            self._title = title
        else:
            raise Exception("raised an exception") 

    title = property(get_title, set_title)
        
    def results(self, new_result=None):
        from classes.result import Result
        if isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results
    
    def players(self, new_player=None):
        from classes.player import Player
        if isinstance(new_player, Player):
            self._players.append(new_player)
        return self._players
    
    def average_score(self, player):
        score = [result.score for result in self._results if player in self._players]
        return sum(score) / len(score)