import numpy as np
import pytest
from source.utilities.ConnectFourScore import ConnectFourScore

@pytest.fixture
def score():
    return ConnectFourScore()

def test_search_spaces_empty(score):

    combinations = np.array([
        [None, None, None, "C"],
        [None, None, "C", None],
        [None, "C", None, None],
        ["C", None, None, None]
        ])

    result = score.search_spaces(combinations, "R")
    assert result == 0

def test_search_spaces_0(score):

    combinations = np.array([
        [None, "Y", "R", "C"],
        ["Y", "R", "C", "R"],
        ["R", "C", "R", None],
        ["C", "R", None, "Y"]
        ])

    result = score.search_spaces(combinations, "R")
    assert result == 0

def test_search_spaces_max(score):

    combinations = np.array([
        ["R", "R", None, "C"],
        ["R", None, "C", None],
        [None, "C", None, "R"],
        ["C", None, "R", "R"]
        ])

    result = score.search_spaces(combinations, "R")
    assert result == 6
    
def test_score_sequence_empty(score):

    combinations = np.array([
        [None, None, None, "C"],
        [None, None, "C", None],
        [None, "C", None, None],
        ["C", None, None, None]
        ])

    result = score.score_sequence(combinations, "R")
    assert result == 0

def test_score_sequence_0(score):

    combinations = np.array([
        [None, None, None, "C"],
        ["Y", "R", "R", "R"],
        ["R", "R", None, "C"],
        ["C", "R", "R", "Y"]
        ])

    result = score.score_sequence(combinations, "R")
    assert result == 0

def test_score_sequence_max(score):

    combinations = np.array([
        ["R", "R", "C", None],
        ["R", "R", "C", None],
        ["R", "C", "R", None],
        [None,"C", "R", "R"]
        ])

    result = score.score_sequence(combinations, "R")
    assert result == 8

def test_score_combinations_0(score):

    combinations = np.array([
        [None, None, None, "Y"],
        ["Y", "R", "R", "R"],
        ["R", "R", None, "Y"],
        ["Y", "R", "R", "Y"]
        ])

    result = score.score_combinations(combinations, "R")
    assert result == 0

def test_score_combinations_max(score):

    combinations = np.array([
        ["R", "R", "R", None],
        ["R", "R", "R", None],
        ["R", None, "R", "R"],
        [None,"R", "R", "R"]
        ])

    result = score.score_combinations(combinations, "R")
    assert result == 12
    