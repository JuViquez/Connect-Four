import numpy as np
from source.games.ConnectFourChecker import ConnectFourChecker
from source.utilities.RandomnessProvider import RandomnessProvider
from source.utilities.ConnectFourScore import ConnectFourScore
from source.utilities.ConnectFourSearcher import ConnectFourSearcher

class ConnectFourStrategy:
    
    def __init__(self, rand_provider):
        self.rand_provider = rand_provider
    
    def secuence(self, board, columns):
        pass
    
    def spaces(self, board, columns, disc):
        subdisc = "r"
        if disc == "Y":
            subdisc = "y"
        checker = ConnectFourChecker()
        score = ConnectFourScore()
        searcher = ConnectFourSearcher()
        row = 0
        max_score = 0
        for i in columns:
            row = checker.simulate_play(board, i)
            board[row][i] = subdisc
            current_score = score.search_spaces(board, searcher.search_horizontal( board, row, i), disc)
            if current_score > max_score:
                max_score = current_score
            current_score = score.search_spaces(board, searcher.search_negative_diagonal( board, row, i), disc)
            if current_score > max_score:
                max_score = current_score
            current_score = score.search_spaces(board, searcher.search_positive_diagonal( board, row, i), disc)
            if current_score > max_score:
                max_score = current_score
            board[row][i] = None
            if max_score == 2:
                return i
        
        
        

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