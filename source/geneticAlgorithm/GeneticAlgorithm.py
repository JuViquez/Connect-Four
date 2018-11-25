import numpy as np
from source.games.ConnectFour import ConnectFour
from source.utilities.RandomnessProvider import RandomnessProvider
from source.geneticAlgorithm.ConnectFourAgentChromosome import ConnectFourAgentChromosome
from source.strategies.ConnectFourStrategy import ConnectFourStrategy
from source.utilities.ConnectFourScore import ConnectFourScore
from source.utilities.ConnectFourSearcher import ConnectFourSearcher
from source.utilities.ConnectFourChecker import ConnectFourChecker

class GeneticAlgorithm:

    def __init__(self, randomness_provider, population_size, children_size):
        self.population = []
        self.population_size = population_size
        self.children_size = children_size
        self.randomness_provider = randomness_provider

    def population_generator(self):
        for i in range(self.population_size):
            strategy = ConnectFourStrategy(self.randomness_provider, ConnectFourChecker(), ConnectFourScore(), ConnectFourSearcher())
            prob_list = self.randomness_provider.gen_rand_prob_list(8)
            agent = ConnectFourAgentChromosome("R", self.randomness_provider, strategy, prob_list)
            self.population.append(np.array([agent, 0]))

    def simulate_matches(self, first_disc, second_disc):
        for agent1 in range(self.population_size):
            for agent2 in range(agent1 + 1, self.population_size):
                if agent1 != agent2:
                    self.population[agent1][0].disc = first_disc
                    self.population[agent2][0].disc = second_disc
                    match =  ConnectFour(self.population[agent1][0], self.population[agent2][0])
                    result = match.turn_manager()
                    if result == first_disc:
                        self.population[agent1][1] += 2
                    elif result == second_disc:
                        self.population[agent2][1] += 2
                    else:
                        self.population[agent1][1] += 1
                        self.population[agent2][1] += 1

    def cross_controller(self):
        probabilities = self.randomness_provider.scale_probs([i[1] for i in ga.population])
        index_list = list(range(self.population_size))
        children = []
        for i in range(self.children_size):
            agent1 = self.randomness_provider.prob_choice(index_list, probabilities)
            agent2 = self.randomness_provider.prob_choice(index_list, probabilities)
            while agent1 == agent2: #Para que no se repitan
                agent2 = self.randomness_provider.prob_choice(index_list, probabilities)
            child = self.population[agent1][0].cross(self.population[agent2][0].strategies_probs)
            children.append(np.array([child, 0]))
        return children

    def mutate_controller(self, children):
        for child in children:
            if self.randomness_provider.random_number(0,1) < 0.1:
                child[0].mutate()

    def replace(self, children):
        for i in range(self.children_size):
            self.population[i] = children[i]

    def genetic_controller(self, generations):
        self.population_generator()
        for i in range(generations):
            print(i)
            self.simulate_matches("R","Y")
            self.simulate_matches("Y","R")
            self.population.sort(key=lambda x: x[1])
            if i != generations - 1:
                children = self.cross_controller()
                self.mutate_controller(children)
                self.replace(children)
        return self.population[-1][0].strategies_probs


ga = GeneticAlgorithm(RandomnessProvider(), 60, 15)
resultado = ga.genetic_controller(20)
print(resultado)