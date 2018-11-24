import numpy as np
from source.agents.ConnectFourAgent import ConnectFourAgent
from source.agents.ConnectFourHumanAgent import ConnectFourHumanAgent
from source.utilities.ConnectFourChecker import ConnectFourChecker
from source.utilities.RandomnessProvider import RandomnessProvider
from source.strategies.ConnectFourStrategy import ConnectFourStrategy
from source.utilities.ConnectFourScore import ConnectFourScore
from source.utilities.ConnectFourSearcher import ConnectFourSearcher

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
        random = RandomnessProvider()
        checker = ConnectFourChecker()
        score = ConnectFourScore()
        searcher = ConnectFourSearcher()
        strategy = ConnectFourStrategy(random, checker, score, searcher)
        self.red = ConnectFourAgent("R",random, strategy,[0.3,0.2,0.05,0.05,0.1,0.1,0.1,0.1])
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
            self.print_board()

    def print_board(self):
        print(" 0 1 2 3 4 5 6 7")
        for row in self.board:
            for column in range(len(row)):
                if row[column] is None:
                    print("| ", end='')
                else:
                    print("|" + row[column], end='')
            print("|")



cf = ConnectFour()
cf.turn_manager()