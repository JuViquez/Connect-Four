import numpy as np

class RandomnessProvider:
    
    def __init__(self):
        pass
    
    def random_int(self, a, b):
        rand_int = np.random.randint(a, b)
        return rand_int
    
    def random_number(self, a, b):
        rand_num = np.random.uniform(a, b)
        return rand_num
    
    def prob_choice(items, probs):
        rand_item = np.random.choice(items, 1, replace=True, p=probs)[0]
        return rand_item

