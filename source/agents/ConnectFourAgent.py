from random import randint
from source.agents.GameAgent import GameAgent
from source.games.ConnectFourChecker import ConnectFourChecker

class ConnectFourAgent(GameAgent):
    
    def __init__(self, disc):
        self._disc = disc
    
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
            return columns[randint(0, column_length-1)] #aquí es donde se llamarían a las estrategias
        return None