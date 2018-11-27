import numpy as np


class ConnectFourSearcher:

    def __init__(self, column_size=6, row_size=7, group_size=4):
        self.column_size = column_size
        self.row_size = row_size
        self.group_size = group_size

    def search_horizontal(self, board, disc_row, disc_column):
        combinations = []
        for i in range(self.group_size):
            lower_index = disc_column - i
            upper_index = lower_index + self.group_size
            if lower_index >= 0 and upper_index <= self.row_size:
                combination = board[disc_row][lower_index: upper_index]
                combinations.insert(0, combination)
        return combinations

    def search_vertical(self, board, disc_row, disc_column):
        combinations = []
        for i in range(self.group_size):
            lower_index = disc_row - i
            upper_index = lower_index + self.group_size
            if lower_index >= 0 and upper_index <= self.column_size:
                combination = board[lower_index:upper_index, disc_column]
                combinations.insert(0, combination)
        return combinations

    def search_negative_diagonal(self, board, disc_row, disc_column):
        combinations = []
        for i in range(self.group_size):
            lower_row_index = disc_row - i
            upper_row_index = lower_row_index + self.group_size
            lower_column_index = disc_column - i
            upper_column_index = lower_column_index + self.group_size
            if(lower_row_index >= 0 and upper_row_index <= self.column_size
               and lower_column_index >= 0 and upper_column_index <= self.row_size):
                mini_board = board[lower_row_index: upper_row_index,
                                   lower_column_index: upper_column_index]
                combination = np.diagonal(mini_board, 0)
                combinations.insert(0, combination)
        return combinations

    def search_positive_diagonal(self, board, disc_row, disc_column):
        combinations = []
        for i in range(self.group_size):
            upper_row_index = disc_row + 1 + i
            lower_row_index = upper_row_index - self.group_size
            lower_column_index = disc_column - i
            upper_column_index = lower_column_index + self.group_size
            if(lower_row_index >= 0 and upper_row_index <= self.column_size
               and lower_column_index >= 0 and upper_column_index <= self.row_size):
                mini_board = board[lower_row_index: upper_row_index,
                                   lower_column_index: upper_column_index]
                combination = np.diagonal(mini_board[::-1], 0)
                combinations.insert(0, combination)
        return combinations
