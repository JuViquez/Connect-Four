import pytest
import numpy as np
from unittest.mock import Mock
from unittest.mock import patch
from source.utilities.RandomnessProvider import RandomnessProvider

@patch('numpy.random.randint', return_value = 0)
def test_random_int(mock_rand_int):
    random = RandomnessProvider()
    random.random_int(0,5)
    mock_rand_int.assert_called_with(0,5)
    
@patch('numpy.random.uniform', return_value = 0)
def test_random_number(mock_rand):
    random = RandomnessProvider()
    random.random_number(0,5.5)
    mock_rand.assert_called_with(0,5.5)
 
@patch('numpy.random.choice')
def test_prob_choice(choice_mock):
        random = RandomnessProvider()
        random.prob_choice([0,1,2], [1,2,4])
        choice_mock.assert_called_with([0,1,2], 1, replace = True, p=[1,2,4])
  
@patch('numpy.random.uniform', return_value = 0)      
def test_gen_rand_prob_list(mock_rand):
        random = RandomnessProvider()
        expected_list = [1,0]
        result = random.gen_rand_prob_list(2)
        assert np.array_equal(expected_list, result)
        mock_rand.asser_called_with(0, 1)
        
def test_scale_probs():
    random = RandomnessProvider()
    probs = [1,1,1,1,1,1,1,1,1,1]
    expected_probs = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
    result = random.scale_probs(probs)
    assert np.array_equal(expected_probs, result)