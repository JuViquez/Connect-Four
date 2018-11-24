from random import randint
from source.agents.GameAgent import GameAgent
from source.utilities.ConnectFourChecker import ConnectFourChecker
from source.strategies.ConnectFourStrategy import ConnectFourStrategy

class ConnectFourAgent(GameAgent):
    
    def __init__(self, disc, rand_provider, strategy, strategies_probs):
        self._disc = disc
        self.rand_provider = rand_provider
        self.strategy = strategy
        self.strategies_probs = strategies_probs
    
    def play(self, board, columns):
        enemy = "Y"
        if self.disc == "Y":
            enemy = "R"
        checker = ConnectFourChecker()
        column_length = len(columns)
        if column_length > 0:
            x = checker.check_win_play(board, columns, self.disc)
            if x is not None: #chequea si se puede ganar
                return x
            x = checker.check_win_play(board, columns, enemy)
            if x is not None: #Chequea si se puede bloquear
                return x
            #return columns[randint(0, column_length-1)] #aquí es donde se llamarían a las estrategias
            return self.strategy.end(board, columns, self.disc)
        return None