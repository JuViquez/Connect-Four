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
from test.FakeRandomnessProvider import FakeRandomnessProvider

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
    controller.board = np.array(
            [[None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, "Y", "Y", None, None],
            [None, None, "R", "Y", "Y", None, "Y"],
            [None, "R", "Y", "R", "R", "R", "Y"]])
    controller.drop_disc(3)
    assert controller.board[2][3] == "R"

def test_play_turn_no_playable_columns(controller):
        controller.board = np.array(
            [["Y", "Y", "Y", "Y", "Y", "Y", "Y"],
            ["Y", "Y", "Y", "Y", "Y", "Y", "Y"],
            ["Y", "Y", "Y", "Y", "Y", "Y", "Y"],
            ["Y", "Y", "Y", "Y", "Y", "Y", "Y"],
            ["Y", "Y", "Y", "Y", "Y", "Y", "Y"],
            ["Y", "Y", "Y", "Y", "Y", "Y", "Y"]])
        assert not controller.play_turn(ConnectFourChecker())

def test_play_turn_R(controller):
        controller.red.strategy.rand_provider = FakeRandomnessProvider(4)
        controller.red.rand_provider = FakeRandomnessProvider(4)
        controller.play_turn(ConnectFourChecker())
        assert controller.board[5][4] == "R"

def test_play_turn_Y(controller):
        controller.turn = "Y"
        controller.yellow.strategy.rand_provider = FakeRandomnessProvider(2)
        controller.yellow.rand_provider = FakeRandomnessProvider(5)
        controller.play_turn(ConnectFourChecker())
        assert controller.board[5][2] == "Y"

def test_turn_manager_R(controller):
        controller.board = np.array(
            [[None, "R", "Y", "Y", "R", "R", "Y"],
            ["Y", "Y", "R", "R", "Y", "Y", "R"],
            ["R", "R", "Y", "Y", "R", "R", "Y"],
            ["Y", "Y", "R", "R", "Y", "Y", "R"],
            ["R", "R", "Y", "Y", "R", "R", "Y"],
            ["Y", "Y", "R", "R", "Y", "Y", "R"]])
        controller.turn_manager(True)
        assert controller.board[0][0] == "R"

def test_turn_manager_Y(controller):
        controller.turn = "Y"
        controller.board = np.array(
            [[None, "R", "Y", "Y", "R", "R", "Y"],
            ["Y", "Y", "R", "R", "Y", "Y", "R"],
            ["R", "R", "Y", "Y", "R", "R", "Y"],
            ["Y", "Y", "R", "R", "Y", "Y", "R"],
            ["R", "R", "Y", "Y", "R", "R", "Y"],
            ["Y", "Y", "R", "R", "Y", "Y", "R"]])
        controller.turn_manager(True)
        assert controller.board[0][0] == "Y"

def test_turn_manager_win_R(controller):
        controller.board = np.array(
            [[None, "R", "R", "R", "Y", "Y", "Y"],
            ["Y", "Y", "R", "R", "Y", "Y", "R"],
            ["R", "R", "Y", "Y", "R", "R", "Y"],
            ["Y", "Y", "R", "R", "Y", "Y", "R"],
            ["R", "R", "Y", "Y", "R", "R", "Y"],
            ["Y", "Y", "R", "R", "Y", "Y", "R"]])
        assert controller.turn_manager(True) == "R"

def test_turn_manager_win_Y(controller):
        controller.turn = "Y"
        controller.board = np.array(
            [[None, "Y", "Y", "Y", "R", "R", "Y"],
            ["Y", "Y", "R", "R", "Y", "Y", "R"],
            ["R", "R", "Y", "Y", "R", "R", "Y"],
            ["Y", "Y", "R", "R", "Y", "Y", "R"],
            ["R", "R", "Y", "Y", "R", "R", "Y"],
            ["Y", "Y", "R", "R", "Y", "Y", "R"]])
        assert controller.turn_manager(True) == "Y"

def test_turn_manager_draw(controller):
        controller.board = np.array(
            [["R", "Y", "Y", "Y", "R", "R", "Y"],
            ["Y", "Y", "R", "R", "Y", "Y", "R"],
            ["R", "R", "Y", "Y", "R", "R", "Y"],
            ["Y", "Y", "R", "R", "Y", "Y", "R"],
            ["R", "R", "Y", "Y", "R", "R", "Y"],
            ["Y", "Y", "R", "R", "Y", "Y", "R"]])
        assert controller.turn_manager(True) == "D"