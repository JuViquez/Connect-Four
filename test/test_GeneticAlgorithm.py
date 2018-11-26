import numpy as np
import pytest
from source.geneticAlgorithm.GeneticAlgorithm import GeneticAlgorithm
from test.FakeRandomnessProvider import FakeRandomnessProvider
from source.utilities.RandomnessProvider import RandomnessProvider

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
    genetic.population_generator()
    genetic.simulate_matches("R","Y")
    genetic.population.sort(key=lambda x: x[1])
    genetic.randomness_provider = RandomnessProvider() #Se cambia el random provider para hacer el cruce
    assert len(genetic.cross_controller()) == 2 

def test_cross_controller_empty(genetic):
    genetic.children_size = 0
    genetic.population_generator()
    genetic.simulate_matches("R","Y")
    assert not genetic.cross_controller()

def test_mutate_controller(genetic):
    """Se manda a mutar los hijos
    como el fake random devuelve 0 la probabilidad de mutar es 100%
    se compara si cambió el cromosoma
    """
    genetic.population_generator()
    genetic.simulate_matches("R","Y")
    genetic.randomness_provider = RandomnessProvider() #Se cambia el random provider para hacer el cruce
    children = genetic.cross_controller()
    child_chromosome = list(children[0][0].strategies_probs)
    genetic.randomness_provider = FakeRandomnessProvider(0) #se restaura el random provider
    genetic.mutate_controller(children)
    assert all(i != j for (i,j) in zip(children[0][0].strategies_probs, child_chromosome))

def test_replace(genetic):
    children = [1,2,3]
    genetic.population_generator()
    genetic.replace(children)
    assert isinstance(genetic.population[0], int)
    assert not isinstance(genetic.population[3], int)

