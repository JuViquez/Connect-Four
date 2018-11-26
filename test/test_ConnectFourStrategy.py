import pytest
import numpy as np
from source.utilities.ConnectFourChecker import ConnectFourChecker
from test.FakeRandomnessProvider import FakeRandomnessProvider
from source.strategies.ConnectFourStrategy import ConnectFourStrategy
from source.utilities.ConnectFourSearcher import ConnectFourSearcher
from source.utilities.ConnectFourScore import ConnectFourScore

@pytest.fixture
def c4_strategy():
    
    checker = ConnectFourChecker()
    score = ConnectFourScore()
    searcher = ConnectFourSearcher()
    fake_random = FakeRandomnessProvider(2.5)
    
    strategy = ConnectFourStrategy(fake_random, checker, score, searcher)
    
    return strategy
    
def test_sequence_without_tie(c4_strategy):
    
    board =  np.array(
            [
            
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None,  'Y',  'R',  'R', None, None]
            
            ])
    expected_column = 5
    valid_columns = list(range(0,7))
    output_column = c4_strategy.sequence(board, valid_columns, "R")
    
    assert expected_column == output_column
    
def test_sequence_with_tie(c4_strategy):
    
    board =  np.array(
            [
            
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, 'R'],
            ['R', 'R', None, None, None, 'R', 'R']
            
            ])
    expected_column = 5
    valid_columns = list(range(0,7))
    output_column = c4_strategy.sequence(board, valid_columns, "R")
    
    assert expected_column == output_column

def test_center_not_full_centers(c4_strategy):
    board =  np.array(
            [
            
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, 'R'],
            ['R', 'R', None, None, None, 'R', 'R']
            
            ])
    expected_column = 3
    valid_columns = list(range(0,7))
    c4_strategy.rand_provider.result = 0
    output_column = c4_strategy.center(board, valid_columns, "R")
    
    assert expected_column == output_column
           
def test_center_tie_centers(c4_strategy):
    board =  np.array(
            [
            
            [None, None, None, 'Y', None, None, None],
            [None, None, None, 'Y', None, None, None],
            [None, None, None, 'Y', None, None, None],
            [None, None, None, 'Y', None, None, None],
            [None, None, None, 'Y', None, None, 'R'],
            ['R', 'R',   None, 'Y', None, 'R', 'R']
            
            ])
    expected_column = 2
    valid_columns = list(range(0,3)) + list(range(4,7))
    c4_strategy.rand_provider.result = 0
    output_column = c4_strategy.center(board, valid_columns, "R")
    
    assert expected_column == output_column
    
def test_center_full_centers(c4_strategy):
    board =  np.array(
            [
            
            [None, None, 'Y', 'Y', 'Y', None, None],
            [None, None, 'Y', 'Y', 'Y', None, None],
            [None, None, 'Y', 'Y', 'Y', None, None],
            [None, None, 'Y', 'Y', 'Y', None, None],
            [None, None, 'Y', 'Y', 'Y', None, 'R'],
            ['R', 'R',   'Y', 'Y', 'Y', 'R', 'R']
            
            ])
    expected_column = 0
    valid_columns = list(range(0,2)) + list(range(5,7))
    c4_strategy.rand_provider.result = 0
    output_column = c4_strategy.center(board, valid_columns, "R")
    
    assert expected_column == output_column


def test_end_not_full_ends(c4_strategy):
    board =  np.array(
            [
            
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, 'R'],
            [None, None, None, None, None, None, 'R']
            
            ])
    expected_column = 6
    valid_columns = list(range(0,7))
    c4_strategy.rand_provider.result = 0
    output_column = c4_strategy.end(board, valid_columns, "R")
    
    assert expected_column == output_column
           
def test_end_tie_ends(c4_strategy):
    board =  np.array(
            [
            
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, 'R', None, None, None],
            [None, None,   None, 'R', None, None,  None]
            
            ])
    expected_column = 1
    valid_columns = list(range(0,7))
    c4_strategy.rand_provider.result = 0
    output_column = c4_strategy.end(board, valid_columns, "R")
    
    assert expected_column == output_column
    
def test_end_full_ends(c4_strategy):
    board =  np.array(
            [
            
            ['R', 'R', None, None, None, 'R', 'R'],
            ['R', 'R', 'Y', 'Y', 'Y', 'R', 'R'],
            ['R', 'R', 'Y', 'Y', 'Y', 'R', 'R'],
            ['R', 'R', 'Y', 'Y', 'Y', 'R', 'R'],
            ['R', 'R', 'Y', 'Y', 'Y', 'R', 'R'],
            ['R', 'R',   'Y', 'Y', 'Y', 'R', 'R']
            
            ])
    expected_column = 2
    valid_columns = list(range(2,5))
    c4_strategy.rand_provider.result = 0
    output_column = c4_strategy.end(board, valid_columns, "R")
    
    assert expected_column == output_column

def test_odd_row(c4_strategy):
    board =  np.array(
            [
            
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None,   None, 'R', None, None,  None]
            
            ])
    expected_column = 4
    valid_columns = list(range(0,7))
    c4_strategy.rand_provider.result = 1
    output_column = c4_strategy.odd_row(board, valid_columns, "R")
    
    assert expected_column == output_column
    
def test_odd_row_full(c4_strategy):
    board =  np.array(
            [
            
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            ['R',   'R',  'R',  'R',  'R',  'R',  'R']
            
            ])
    expected_column = 0
    valid_columns = list(range(0,7))
    c4_strategy.rand_provider.result = 0
    output_column = c4_strategy.odd_row(board, valid_columns, "R")
    
    assert expected_column == output_column
    
def test_odd_row_tie(c4_strategy):
    board =  np.array(
            [
            
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            ['R',  None,  'R',  'R', 'R',  None,  'R']
            
            ])
    expected_column = 1
    valid_columns = list(range(0,7))
    c4_strategy.rand_provider.result = 0
    output_column = c4_strategy.odd_row(board, valid_columns, "R")
    
    assert expected_column == output_column

def test_even_row(c4_strategy):
    board =  np.array(
            [
            
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None,   None, 'R', None, None,  None]
            
            ])
    expected_column = 3
    valid_columns = list(range(0,7))
    c4_strategy.rand_provider.result = 0
    output_column = c4_strategy.even_row(board, valid_columns, "R")
    
    assert expected_column == output_column
    
def test_even_row_full(c4_strategy):
    board =  np.array(
            [
            
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            ['R',   'R',  'R',  'R',  'R',  'R',  'R'],
            ['R',   'R',  'R',  'R',  'R',  'R',  'R']
            
            ])
    expected_column = 0
    valid_columns = list(range(0,7))
    c4_strategy.rand_provider.result = 0
    output_column = c4_strategy.even_row(board, valid_columns, "R")
    
    assert expected_column == output_column
    
def test_even_row_tie(c4_strategy):
    board =  np.array(
            [
            
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            ['R',  None,  'R',  'R', 'R',  None,  'R'],
            ['R',   'R',  'R',  'R',  'R',  'R',  'R']
            
            ])
    expected_column = 1
    valid_columns = list(range(0,7))
    c4_strategy.rand_provider.result = 0
    output_column = c4_strategy.even_row(board, valid_columns, "R")
    
    assert expected_column == output_column
  
