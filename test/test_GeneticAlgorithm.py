import numpy as np
import pytest
from source.geneticAlgorithm.GeneticAlgorithm import GeneticAlgorithm
from test.FakeRandomnessProvider import FakeRandomnessProvider

@pytest.fixture
def genetic():
    return GeneticAlgorithm(FakeRandomnessProvider(0),4,2)

def test_population_generator(genetic):
    genetic.population_generator()
    assert len(genetic.population) == 4

def test_population_generator_empty(genetic):
    genetic.population_size = 0
    genetic.population_generator()
    assert not len(genetic.population)

def test_simulate_matches(genetic):
    """Simula los 6 partidos ya que son 4 agentes
    cada partido reparte 2 pts, por lo tanto, se compara con 12 pts
    """
    genetic.population_generator()
    genetic.simulate_matches("R","Y")
    total_points = 0
    for i in genetic.population:
        total_points += i[1]
    assert total_points == 12 

def test_cross_controller(genetic):
    assert len(genetic.cross_controller()) == 2 

def test_cross_controller_empty(genetic):
    genetic.children_size = 0
    assert not genetic.cross_controller()