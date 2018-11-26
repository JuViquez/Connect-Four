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