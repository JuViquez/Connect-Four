import numpy as np

class ConnectFour():
    def __init__(self):
        self.red = None
        self.yellow = None
        self.board = np.array(
            [[None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None]])
    
    def check_win(self, value):
        for c in range(4):
            for r in range(6):
                if self.board[r][c] == value and self.board[r][c+1] == value and self.board[r][c+2] == value and self.board[r][c+3] == value:
                    return True
        for c in range(7):
            for r in range(3):
                if self.board[r][c] == value and self.board[r+1][c] == value and self.board[r+2][c] == value and self.board[r+3][c] == value:
                    return True
        for c in range(4):
            for r in range(3):
                if self.board[r][c] == value and self.board[r+1][c+1] == value and self.board[r+2][c+2] == value and self.board[r+3][c+3] == value:
                    return True
        for c in range(4):
            for r in range(3, 6):
                if self.board[r][c] == value and self.board[r-1][c+1] == value and self.board[r-2][c+2] == value and self.board[r-3][c+3] == value:
                    return True
        return False