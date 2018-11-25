import argparse
from source.utilities.RandomnessProvider import RandomnessProvider
from source.geneticAlgorithm.GeneticAlgorithm import GeneticAlgorithm

def init_gen():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pop-size", required = True, type = int)
    parser.add_argument("--children", required = True, type = int)
    parser.add_argument("--generations", required = True, type = int)
    args = parser.parse_args()
    
    ga = GeneticAlgorithm(RandomnessProvider(), args.pop_size, args.children)
    resultado = ga.genetic_controller(args.generations)
    print(resultado)
    
if __name__ == "__main__":
    init_gen()