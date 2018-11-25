import numpy as np
from source.agents.ConnectFourAgent import ConnectFourAgent
from source.agents.ConnectFourHumanAgent import ConnectFourHumanAgent
from source.utilities.ConnectFourChecker import ConnectFourChecker
from source.utilities.RandomnessProvider import RandomnessProvider
from source.strategies.ConnectFourStrategy import ConnectFourStrategy
from source.utilities.ConnectFourScore import ConnectFourScore
from source.utilities.ConnectFourSearcher import ConnectFourSearcher
from source.utilities.settings import FIRST_PLAY

class ConnectFour():
    def __init__(self, red, yellow):
        self.turn = FIRST_PLAY
        self.red = red
        self.yellow = yellow
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
        checker = ConnectFourChecker()
        """
        random = RandomnessProvider()
        score = ConnectFourScore()
        searcher = ConnectFourSearcher()
        strategy = ConnectFourStrategy(random, checker, score, searcher)
        """
        #self.red = ConnectFourAgent("R",random, strategy,[0.3,0.2,0.05,0.05,0.1,0.1,0.1,0.1])
        #self.yellow = ConnectFourHumanAgent("Y")
        checker = ConnectFourChecker()
        winner = ""
        game_over = False
        while(not game_over):
            if not self.play_turn(checker): #tablero lleno, empate
                #print("Draw")
                #self.print_board()
                game_over = True
                winner = "D"
            elif checker.check_win(self.board, self.turn): #hay ganador
                #print("Winner winner chicken dinner " + self.turn)
                #self.print_board()
                game_over = True
                winner = self.turn
            else: #cambio de turno
                if self.turn == "R":
                    self.turn = "Y"
                else:
                    self.turn = "R"
                #print("---------------------------------------------------------------")
                #self.print_board()
        return winner

    def print_board(self):
        print("  0 1 2 3 4 5 6")
        for row in range(len(self.board)):
            print(row, end='')
            for column in range(len(self.board[row])):
                if self.board[row][column] is None:
                    print("| ", end='')
                else:
                    print("|" + self.board[row][column], end='')
            print("|")



#cf = ConnectFour()
#cf.turn_manager()