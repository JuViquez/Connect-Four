import numpy as np
from source.utilities.ConnectFourChecker import ConnectFourChecker
from source.utilities.RandomnessProvider import RandomnessProvider
from source.utilities.ConnectFourScore import ConnectFourScore
from source.utilities.ConnectFourSearcher import ConnectFourSearcher

class ConnectFourStrategy:
    
    def __init__(self, rand_provider, checker, score, searcher):
        self.rand_provider = rand_provider
        self.checker = checker
        self.searcher = searcher
        self.score = score
    
    def secuence(self, board, columns, disc):
        subdisc = "C"
        row = 0
        max_score = 0
        best_columns = []
        for column in columns:
            row = self.checker.simulate_play(board, column)
            board[row][columns] = subdisc
            
            combinations = self.searcher.search_horizontal(board, row, column)
            current_score = self.score.score_sequence(combinations, disc)
            
            combinations = self.searcher.search_vertical(board, row, column)
            current_score += self.score.score_sequence(combinations, disc)
            
            combinations = self.searcher.search_negative_diagonal(board, row, column)
            current_score += self.score.score_sequence(combinations, disc)
            
            combinations = self.searcher.search_positive_diagonal(board, row, column)
            current_score += self.score.score_sequence(combinations, disc)
            
            board[row][column] = None
            
            if max_score < current_score:
                max_score = current_score
                best_columns = []
                best_columns.append(column)
            elif max_score == current_score:
                best_columns.append(column)       
        
        best_column = self.rand_provider.prob_choice(best_columns, None)
        return best_column
    
    def spaces(self, board, columns, disc):
        subdisc = "r"
        if disc == "Y":
            subdisc = "y"
        checker = ConnectFourChecker()
        score = ConnectFourScore()
        searcher = ConnectFourSearcher()
        row = 0
        max_score = 0
        best_column = -1
        for i in columns:
            row = checker.simulate_play(board, i)
            board[row][i] = subdisc
            current_score = score.search_spaces(board, searcher.search_horizontal(board, row, i), disc)
            if current_score > max_score:
                max_score = current_score
                best_column = i
            current_score = score.search_spaces(board, searcher.search_negative_diagonal(board, row, i), disc)
            if current_score > max_score:
                max_score = current_score
                best_column = i
            current_score = score.search_spaces(board, searcher.search_positive_diagonal(board, row, i), disc)
            if current_score > max_score:
                max_score = current_score
                best_column = i
            board[row][i] = None
            if max_score == 2:
                return i
        return best_column

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