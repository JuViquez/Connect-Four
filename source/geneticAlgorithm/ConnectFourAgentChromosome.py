import numpy as np
from source.agents.ConnectFourAgent import ConnectFourAgent
from source.geneticAlgorithm.Chromosome import Chromosome

class ConnectFourAgentChromosome(ConnectFourAgent, Chromosome):
    
    def __init__(self, disc, rand_provider, strategy, strategies_probs):
        ConnectFourAgent.__init__(self, disc, rand_provider, 
                                  strategy, strategies_probs)
    
    def mutate(self):
        len_probs = len(self.strategies_probs)
        prob_idx = self.rand_provider.random_int(0, len_probs)
        mutation = self.rand_provider.random_number(0, 1)
        self.strategies_probs[prob_idx] = mutation
        self.strategies_probs = self.rand_provider.scale_probs(self.strategies_probs)
        
    def cross(self, chromosome):
        len_probs = len(self.strategies_probs)
        split_idx = self.rand_provider.random_int(0, len_probs)
        self_half = self.strategies_probs[0 : split_idx] 
        chr_half = chromosome[split_idx, len_probs]
        new_probs = np.concatenate((self_half, chr_half))
        new_probs = self.rand_provider.scale_probs(new_probs)
        
        new_chromosome = ConnectFourAgentChromosome(self.disc, self.rand_provider,
                                                    self.strategy, new_probs)
        
        return new_chromosome