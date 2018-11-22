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
    
    def prob_choice(self, items, probs):
        rand_item = np.random.choice(items, 1, replace=True, p=probs)[0]
        return rand_item

    def gen_rand_prob_list(self, n_probs):
        remaining_prob = 1.0
        probs = np.empty(0)
        for i in range(n_probs-1):
            rand_num = np.random.uniform(0, remaining_prob)
            probs = np.insert(probs, 0, rand_num)
            remaining_prob = remaining_prob - rand_num
        probs = np.insert(probs, 0, remaining_prob)
        return probs
    
    def scale_probs(probs):
        total_prob = sum(probs)
        size_probs = len(probs)
        for i in range(size_probs):
            probs[i] = probs[i] / total_prob
        return probs