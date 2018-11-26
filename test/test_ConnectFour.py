import numpy as np
import pytest
from source.games.ConnectFour import ConnectFour
from source.agents.ConnectFourAgent import ConnectFourAgent
from source.agents.ConnectFourHumanAgent import ConnectFourHumanAgent
from source.utilities.ConnectFourChecker import ConnectFourChecker
from source.utilities.RandomnessProvider import RandomnessProvider
from source.strategies.ConnectFourStrategy import ConnectFourStrategy
from source.utilities.ConnectFourScore import ConnectFourScore
from source.utilities.ConnectFourSearcher import ConnectFourSearcher

@pytest.fixture
def controller():
    rand = RandomnessProvider()
    checker = ConnectFourChecker()
    scorer = ConnectFourScore()
    searcher = ConnectFourSearcher()
    strategy = ConnectFourStrategy(rand, checker, scorer, searcher)
    red = ConnectFourAgent("R", rand, strategy, [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125])
    yellow = ConnectFourAgent("Y", rand, strategy, [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125])
    connect_four = ConnectFour(red, yellow)
    return connect_four

def test_drop_disc_empty(controller):
    controller.drop_disc(0)
    assert controller.board[-1][0] == "R"

def test_drop_disc_full(controller):
    controller.board = np.array(
            [["Y", "Y", "Y", "Y", "Y", "Y", "Y"],
            ["Y", "Y", "Y", "Y", "Y", "Y", "Y"],
            ["Y", "Y", "Y", "Y", "Y", "Y", "Y"],
            ["Y", "Y", "Y", "Y", "Y", "Y", "Y"],
            ["Y", "Y", "Y", "Y", "Y", "Y", "Y"],
            ["Y", "Y", "Y", "Y", "Y", "Y", "Y"]])
    controller.drop_disc(0)
    assert controller.board[0][0] == "Y" 
    
def test_drop_disc(controller):
    controller.board = new_board = np.array(
            [[None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, "Y", "Y", None, None],
            [None, None, "R", "Y", "Y", None, "Y"],
            [None, "R", "Y", "R", "R", "R", "Y"]])
    controller.drop_disc(3)
    assert controller.board[2][3] == "R"