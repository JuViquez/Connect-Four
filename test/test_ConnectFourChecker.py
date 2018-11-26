import numpy as np
import pytest
from source.utilities.ConnectFourChecker import ConnectFourChecker

@pytest.fixture
def board():
    board = np.array(
            [[None, None, "R", None, "R", None, None],
            ["R", None, "Y", None, "Y", None, None],
            ["R", "R", "Y", None, "R", None, None],
            ["Y", "Y", "Y", "R", "Y", None, None],
            ["Y", "R", "R", "R", "Y", None, None],
            ["Y", "Y", "R", "R", "Y", None, None]])
    return board

@pytest.fixture
def checker():
    return ConnectFourChecker()

def test_possible_plays(checker, board):

    assert checker.possible_plays(board) == [0,1,3,5,6]

def test_possible_plays_empty(checker, board):
    empty_board = np.array(
            [[None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None]])
    assert checker.possible_plays(empty_board) == [0,1,2,3,4,5,6]

def test_possible_plays_full(checker, board):
    full_board = np.array(
            [["R", "R", "R", "R", "R", "R", "R"],
            ["R", "R", "R", "R", "R", "R", "R"],
            ["R", "R", "R", "R", "R", "R", "R"],
            ["R", "R", "R", "R", "R", "R", "R"],
            ["R", "R", "R", "R", "R", "R", "R"],
            ["R", "R", "R", "R", "R", "R", "R"]])
    assert len(checker.possible_plays(full_board)) == 0
    
def test_simulate_play(checker, board):
    assert checker.simulate_play(board, 0) == 0
    assert checker.simulate_play(board, 3) == 2
    assert checker.simulate_play(board, 2) is None

def test_check_win_play_None(checker, board):
    assert checker.check_win_play(board, [0,1,3,5,6], "Y") is None

def test_check_win_play_vertical(checker, board):
    assert checker.check_win_play(board, [0,1,3,5,6], "R") == 3

def test_check_win_play_horizontal(checker):
    new_board = np.array(
            [[None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, "Y", "Y", None, None],
            [None, None, "R", "Y", "Y", None, "Y"],
            [None, "R", "Y", "R", "R", "R", "Y"]])
    assert checker.check_win_play(new_board, [0,1,2,3,4,5,6], "Y") == 5

def test_check_win_play_positive_diagonal(checker):
    new_board = np.array(
            [[None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, "R", "Y", None, None],
            [None, None, "R", "Y", "Y", None, None],
            [None, "R", "Y", "R", "R", None, None]])
    assert checker.check_win_play(new_board, [0,1,2,3,4,5,6], "R") == 4

def test_check_win_play_negative_diagonal(checker):
    new_board = np.array(
            [[None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, "Y", None, None, None, None, None],
            [None, "R", None, None, None, None, None],
            [None, "Y", "R", "Y", None, None, None],
            [None, "R", "Y", "R", "Y", None, None]])
    assert checker.check_win_play(new_board, [0,1,2,3,4,5,6], "Y") == 2

def test_check_win_vertical(checker):
    new_board = np.array(
            [[None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, "R", "R", "R", "R", None, None]])
    assert checker.check_win(new_board, "R")

def test_check_win_horizontal(checker):
    new_board = np.array(
            [[None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, "R", None, None, None, None, None],
            [None, "R", None, None, None, None, None],
            [None, "R", None, None, None, None, None],
            [None, "R", None, None, None, None, None]])
    assert checker.check_win(new_board, "R")

def test_check_win_positive_diagonal(checker):
    new_board = np.array(
            [[None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, "R", None, None],
            [None, None, None, "R", None, None, None],
            [None, None, "R", None, None, None, None],
            [None, "R", None, None, None, None, None]])
    assert checker.check_win(new_board, "R")

def test_check_win_negative_diagonal(checker):
    new_board = np.array(
            [[None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            ["R", None, None, None, None, None, None],
            [None, "R", None, None, None, None, None],
            [None, None, "R", None, None, None, None],
            [None, None, None, "R", None, None, None]])
    assert checker.check_win(new_board, "R")

def test_check_win_false(checker):
    new_board = np.array(
            [[None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            ["R", None, None, None, None, None, None],
            [None, "R", None, None, None, None, None],
            [None, None, "R", None, None, None, None],
            [None, None, None, "R", None, None, None]])
    assert not checker.check_win(new_board, "Y")