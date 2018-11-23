import numpy as np
from source.agents.ConnectFourAgent import ConnectFourAgent
from source.agents.ConnectFourHumanAgent import ConnectFourHumanAgent
from source.utilities.ConnectFourChecker import ConnectFourChecker
from source.utilities.RandomnessProvider import RandomnessProvider
from source.strategies.ConnectFourStrategy import ConnectFourStrategy

class ConnectFour():
    def __init__(self):
        self.turn = "R"
        self.red = None
        self.yellow = None
        self.board = np.array(
            [[None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None]])

    def drop_disc(self, column):
        for i in range(1,7):
            if self.board[i*-1][column] is None:
                self.board[i*-1][column] = self.turn
                break
    
    def play_turn(self, checker):
        playable_columns = checker.possible_plays(self.board)
        if len(playable_columns) > 0:
            if self.turn == "R":
                column = self.red.play(self.board, playable_columns)
            else:
                column = self.yellow.play(self.board, playable_columns)
            self.drop_disc(column)
            return True
        else:
            return False

    def turn_manager(self):
        self.red = ConnectFourAgent("R",RandomnessProvider(),ConnectFourStrategy(RandomnessProvider()),[])
        self.yellow = ConnectFourHumanAgent("Y")
        checker = ConnectFourChecker()
        game_over = False
        while(not game_over):
            if not self.play_turn(checker): #tablero lleno, empate
                print("Draw")
                game_over = True
            elif checker.check_win(self.board, self.turn): #hay ganador
                print("Winner winner chicken dinner " + self.turn)
                game_over = True
            else: #cambio de turno
                if self.turn == "R":
                    self.turn = "Y"
                else:
                    self.turn = "R"
                print("---------------------------------------------------------------")
                print(self.board)



cf = ConnectFour()
cf.turn_manager()