import numpy as np
import pytest
from source.agents.ConnectFourAgent import ConnectFourAgent
from source.agents.ConnectFourHumanAgent import ConnectFourHumanAgent
from source.utilities.ConnectFourChecker import ConnectFourChecker
from source.utilities.RandomnessProvider import RandomnessProvider
from source.strategies.ConnectFourStrategy import ConnectFourStrategy
from source.utilities.ConnectFourScore import ConnectFourScore
from source.utilities.ConnectFourSearcher import ConnectFourSearcher
from test.FakeRandomnessProvider import FakeRandomnessProvider

@pytest.fixture
def agent():
    rand = RandomnessProvider()
    checker = ConnectFourChecker()
    scorer = ConnectFourScore()
    searcher = ConnectFourSearcher()
    strategy = ConnectFourStrategy(rand, checker, scorer, searcher)
    yellow = ConnectFourAgent("Y", rand, strategy, [0, 0, 0, 0, 0, 0 , 0, 1])
    return yellow

def test_play_win(agent):
    board = np.array([
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, "Y", "Y", None, "Y", None, None]
    ])

    win_column = agent.play(board, [0, 1, 2, 3, 4, 5, 6])
    assert win_column == 3

def test_play_block(agent):
    board = np.array([
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, "R", "R", None, "R", None]
    ])

    block_column = agent.play(board, [0, 1, 2, 3, 4, 5, 6])
    assert block_column == 4

def test_play_empty(agent):
    assert not agent.play([], [])

def test_play(agent):
    board = np.array([
        [None, None, "R", "R", "Y", "Y", "R"],
        [None, None, "R", "R", "Y", "Y", "R"],
        [None, None, "Y", "Y", "R", "R", "Y"],
        [None, None, "Y", "Y","R", "R", "Y"],
        [None, None, "R", "R", "Y", "Y", "R"],
        [None, None, "Y", "Y", "R", "R", "Y"]
    ])

    result_column = agent.play(board, [0, 1])
    assert result_column == 0