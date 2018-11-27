from random import randint
from source.agents.GameAgent import GameAgent
from source.utilities.ConnectFourChecker import ConnectFourChecker
from source.strategies.ConnectFourStrategy import ConnectFourStrategy


class ConnectFourAgent(GameAgent):

    def __init__(self, disc, rand_provider, strategy, strategies_probs):
        self._disc = disc
        self.should_print = False
        self.rand_provider = rand_provider
        self.strategy = strategy
        self.strategies_probs = strategies_probs
        self.strategies = {
            "Secuencia": self.strategy.sequence,
            "Espacios": self.strategy.spaces,
            "Centros": self.strategy.center,
            "Extremos": self.strategy.end,
            "Fila Impar": self.strategy.odd_row,
            "Fila Par": self.strategy.even_row,
            "Columna Impar": self.strategy.odd_column,
            "Columna Par": self.strategy.even_column}

    def play(self, board, columns):
        enemy = "Y"
        if self.disc == "Y":
            enemy = "R"
        checker = ConnectFourChecker()
        column_length = len(columns)
        if column_length > 0:
            x = checker.check_win_play(board, columns, self.disc)
            if x is not None:  # chequea si se puede ganar
                if self.should_print:
                    print("Se escogio una jugada ganadora")
                return x
            x = checker.check_win_play(board, columns, enemy)
            if x is not None:  # Chequea si se puede bloquear
                if self.should_print:
                    print("Se bloqueo una jugada enemiga")
                return x
            strategies_keys = [
                "Secuencia",
                "Espacios",
                "Centros",
                "Extremos",
                "Fila Impar",
                "Fila Par",
                "Columna Impar",
                "Columna Par"]
            selected_str = self.rand_provider.prob_choice(
                strategies_keys, self.strategies_probs)
            strategy_method = self.strategies.get(selected_str)
            columna = strategy_method(board, columns, self.disc)
            if self.should_print:
                print("Estrategia elegida: " + str(selected_str) + " columna: " + str(columna))
            return columna
        return None
