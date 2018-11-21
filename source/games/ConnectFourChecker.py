import numpy as np

class ConnectFourChecker():
    
    def possible_plays(self, board):
        possible = []
        for i in range(7):
            if board[0][i] is None:
                possible.append(i)
        return possible

    def simulate_play(self, board, column):
        for i in range(1,7):
            if board[i*-1][column] is None:
                return i*-1

    def check_win_play(self, board, columns, value):
        for i in columns:
            row = self.simulate_play(board, i)
            board[row][i] = value
            if self.check_win(board, value):
                board[row][i] = None
                return i
            board[row][i] = None
        return None

    def check_win(self, board, value):
        for c in range(4):
            for r in range(6):
                if board[r][c] == value and board[r][c+1] == value and board[r][c+2] == value and board[r][c+3] == value:
                    return True
        for c in range(7):
            for r in range(3):
                if board[r][c] == value and board[r+1][c] == value and board[r+2][c] == value and board[r+3][c] == value:
                    return True
        for c in range(4):
            for r in range(3):
                if board[r][c] == value and board[r+1][c+1] == value and board[r+2][c+2] == value and board[r+3][c+3] == value:
                    return True
        for c in range(4):
            for r in range(3, 6):
                if board[r][c] == value and board[r-1][c+1] == value and board[r-2][c+2] == value and board[r-3][c+3] == value:
                    return True
        return False