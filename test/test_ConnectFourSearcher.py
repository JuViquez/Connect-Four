import numpy as np
import pytest
from source.utilities.ConnectFourSearcher import ConnectFourSearcher

@pytest.fixture
def board():
    board = np.array(
            [
            ['0-0', '0-1', '0-2', '0-3', '0-4', '0-5', '0-6'],
            ['1-0', '1-1', '1-2', '1-3', '1-4', '1-5', '1-6'],
            ['2-0', '2-1', '2-2', '2-3', '2-4', '2-5', '2-6'],
            ['3-0', '3-1', '3-2', '3-3', '3-4', '3-5', '3-6'],
            ['4-0', '4-1', '4-2', '4-3', '4-4', '4-5', '4-6'],
            ['5-0', '5-1', '5-2', '5-3', '5-4', '5-5', '5-6']
            ])
    return board

def test_search_horizontal(board):
    searcher = ConnectFourSearcher()
    
    combinations = [
                    ['5-0', '5-1', '5-2', '5-3'],
                    ['5-1', '5-2', '5-3', '5-4'],
                    ['5-2', '5-3', '5-4', '5-5'],
                    ['5-3', '5-4', '5-5', '5-6'] 
                  ]
    real_combinations = searcher.search_horizontal(board, 5, 3)
    assert np.array_equal(combinations, real_combinations)
    
def test_search_vertical(board): 
    searcher = ConnectFourSearcher()
    
    combinations = [
                    ['2-3', '3-3', '4-3', '5-3']
                   ]
    real_combinations = searcher.search_vertical(board, 5, 3)
    assert np.array_equal(combinations, real_combinations)
    
def test_search_negative_diagonal(board):
    searcher = ConnectFourSearcher()
    
    combinations = [
                    ['2-0', '3-1', '4-2', '5-3']
                   ]
    real_combinations = searcher.search_negative_diagonal(board, 5, 3)
    assert np.array_equal(combinations, real_combinations)

def test_search_positive_diagonal(board):
    searcher = ConnectFourSearcher()
    
    combinations = [
                    ['5-3', '4-4', '3-5', '2-6']
                   ]
    real_combinations = searcher.search_positive_diagonal(board, 5, 3)
    assert np.array_equal(combinations, real_combinations)