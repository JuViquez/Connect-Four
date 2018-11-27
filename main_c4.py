import argparse
from source.agents.ConnectFourAgent import ConnectFourAgent
from source.agents.ConnectFourHumanAgent import ConnectFourHumanAgent
from source.games.ConnectFour import ConnectFour
from source.strategies.ConnectFourStrategy import ConnectFourStrategy
from source.utilities.RandomnessProvider import RandomnessProvider
from source.utilities.ConnectFourChecker import ConnectFourChecker
from source.utilities.ConnectFourScore import ConnectFourScore
from source.utilities.ConnectFourSearcher import ConnectFourSearcher
import source.utilities.settings as system_settings

def init_game():
    parser = argparse.ArgumentParser()
    parser.add_argument("-RedIA", action = "store_true", help = 'rojo sera un agente')
    parser.add_argument("-YellowIA", action = "store_true", help = 'amarillo sera un agente')
    
    args = parser.parse_args()
    
    red = ConnectFourHumanAgent('R')
    yellow = ConnectFourHumanAgent('Y')
    if args.RedIA or args.YellowIA:
        rand = RandomnessProvider()
        checker = ConnectFourChecker()
        scorer = ConnectFourScore()
        searcher = ConnectFourSearcher()
        strategy = ConnectFourStrategy(rand, checker, scorer, searcher)
        if args.RedIA:
            red = ConnectFourAgent("R", rand, strategy, system_settings.R_STRATEGIES_PROBS)
        if args.YellowIA:
            yellow = ConnectFourAgent("Y", rand, strategy, system_settings.Y_STRATEGIES_PROBS)
    
    c4 = ConnectFour(red, yellow)
    c4.turn_manager(True)

if __name__ == "__main__":
    init_game()