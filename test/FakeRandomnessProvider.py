import numpy as np
from source.utilities.RandomnessProvider import RandomnessProvider

class FakeRandomnessProvider(RandomnessProvider):
    
    def __init__(self):
        super().__init__()
    
    def random_int(self, a, b):
        return b//2
    
    def random_number(self, a, b):
        return b/2
    
    def prob_choice(self, items, probs):
        return items[0]
    
    def gen_rand_prob_list(self, n_probs):
        return np.full((n_probs), 1/n_probs)
    
