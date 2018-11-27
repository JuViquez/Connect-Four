import pytest
import numpy as np
from test.FakeRandomnessProvider import FakeRandomnessProvider
from source.geneticAlgorithm.ConnectFourAgentChromosome import ConnectFourAgentChromosome
from source.strategies.ConnectFourStrategy import ConnectFourStrategy

@pytest.fixture
def chromosome():
    rand = FakeRandomnessProvider(0)
    strategies_probs = [0.4, 0.3, 0.3]
    strategy = ConnectFourStrategy(rand, None, None, None)
    chromosome = ConnectFourAgentChromosome(None, rand, strategy, strategies_probs)
    return chromosome
    
def test_mutate(chromosome):
    chromosome.mutate()
    expected_mutation = [0, 0.5, 0.5]
    assert np.array_equal(chromosome.strategies_probs, expected_mutation)
    
def test_cross(chromosome):
    chromosome2 = chromosome
    chromosome2.strategies_probs = [0.3, 0.3, 0.4]
    expected_probs = [0.3, 0.3, 0.4]
    child = chromosome.cross(chromosome2.strategies_probs)
    
    assert np.array_equal(child.strategies_probs, expected_probs)