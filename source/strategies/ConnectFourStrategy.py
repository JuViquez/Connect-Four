import numpy as np
from source.games.ConnectFourChecker import ConnectFourChecker
from source.utilities.RandomnessProvider import RandomnessProvider

class ConnectFourStrategy:
    
    def __init__(self, rand_provider):
        self.rand_provider = rand_provider
    
    def secuence(self, board, columns):
        pass
    
    def spaces(self, board, columns, value):
        """
        checker = ConnectFourChecker()
        row = 0
        for i in columns:
            row = checker.simulate_play(board, i)
            board[row][i] = value
            board[row][i] = None
        """

    def center(self, board, columns):
        centers = []
        for i in columns:
            if i > 1 and i < 5:
                centers.append(i)
        if len(centers) > 0:
            return self.rand_provider.prob_choice(centers,None) 
    
    def end(self, board, columns):
        ends = []
        for i in columns:
            if i < 2 and i > 4:
                ends.append(i)
        if len(ends) > 0:
            return self.rand_provider.prob_choice(ends,None)
    
    def odd_row(self, board, columns):
        pass
    
    def even_row(self, board, columns):
        pass
    
    def odd_column(self, board, columns):
        pass
    
    def even_column(self, board, columns):
        pass