import numpy as np
from source.utilities.ConnectFourChecker import ConnectFourChecker
from source.utilities.RandomnessProvider import RandomnessProvider
from source.utilities.ConnectFourScore import ConnectFourScore
from source.utilities.ConnectFourSearcher import ConnectFourSearcher


class ConnectFourStrategy:

    def __init__(self, rand_provider, checker, score, searcher):
        self.rand_provider = rand_provider
        self.checker = checker
        self.searcher = searcher
        self.score = score

    def sequence(self, board, columns, disc):
        subdisc = "C"
        row = 0
        max_score = 0
        best_columns = []
        for column in columns:
            row = self.checker.simulate_play(board, column)
            board[row][column] = subdisc

            combinations = self.searcher.search_horizontal(board, row, column)
            current_score = self.score.score_sequence(combinations, disc)

            combinations = self.searcher.search_vertical(board, row, column)
            current_score += self.score.score_sequence(combinations, disc)

            combinations = self.searcher.search_negative_diagonal(
                board, row, column)
            current_score += self.score.score_sequence(combinations, disc)

            combinations = self.searcher.search_positive_diagonal(
                board, row, column)
            current_score += self.score.score_sequence(combinations, disc)

            board[row][column] = None

            if max_score < current_score:
                max_score = current_score
                best_columns = []
                best_columns.append(column)
            elif max_score == current_score:
                best_columns.append(column)
        best_column = self.rand_provider.prob_choice(best_columns, None)
        return best_column

    def spaces(self, board, columns, disc):
        draw = []
        row = 0
        max_score = 0
        for i in columns:
            row = self.checker.simulate_play(board, i)
            board[row][i] = "C"
            horizontal = self.searcher.search_horizontal(board, row, i)
            negative_diagonal = self.searcher.search_negative_diagonal(
                board, row, i)
            positive_diagonal = self.searcher.search_positive_diagonal(
                board, row, i)
            current_score = (
                self.score.search_spaces(
                    horizontal,
                    disc) +
                self.score.search_spaces(
                    negative_diagonal,
                    disc) +
                self.score.search_spaces(
                    positive_diagonal,
                    disc))
            if current_score > max_score:
                draw = []
                draw.append(i)
                max_score = current_score
            elif current_score == max_score:
                draw.append(i)
            board[row][i] = None
        return self.rand_provider.prob_choice(draw, None)

    def center(self, board, columns, disc):
        centers = []
        for i in columns:
            if i > 1 and i < 5:
                centers.append(i)
        max_score = 0
        best_columns = []
        for center in centers:
            row = self.checker.simulate_play(board, center)
            current_score = self.__calculate_score(board, row, center, disc)
            if max_score < current_score:
                max_score = current_score
                best_columns = []
                best_columns.append(center)
            elif max_score == current_score:
                best_columns.append(center)
            board[row][center] = None
        if not centers:
            best_columns = columns
        best_column = self.rand_provider.prob_choice(best_columns, None)
        return best_column

    def end(self, board, columns, disc):
        ends = []
        for i in columns:
            if i < 2 or i > 4:
                ends.append(i)
        max_score = 0
        best_columns = []
        for end in ends:
            row = self.checker.simulate_play(board, end)
            current_score = self.__calculate_score(board, row, end, disc)
            if max_score < current_score:
                max_score = current_score
                best_columns = []
                best_columns.append(end)
            elif max_score == current_score:
                best_columns.append(end)
            board[row][end] = None
        if not ends:
            best_columns = columns
        best_column = self.rand_provider.prob_choice(best_columns, None)
        return best_column

    def odd_row(self, board, columns, disc):
        odds = []
        for i in columns:
            row = self.checker.simulate_play(board, i)
            if row % 2 == 1:
                odds.append(i)
        max_score = 0
        best_columns = []
        for odd in odds:
            row = self.checker.simulate_play(board, odd)
            current_score = self.__calculate_score(board, row, odd, disc)
            if max_score < current_score:
                max_score = current_score
                best_columns = []
                best_columns.append(odd)
            elif max_score == current_score:
                best_columns.append(odd)
            board[row][odd] = None
        if not odds:
            best_columns = columns
        best_column = self.rand_provider.prob_choice(best_columns, None)
        return best_column

    def even_row(self, board, columns, disc):
        evens = []
        for i in columns:
            row = self.checker.simulate_play(board, i)
            if row % 2 == 0:
                evens.append(i)
        max_score = 0
        best_columns = []
        for even in evens:
            row = self.checker.simulate_play(board, even)
            current_score = self.__calculate_score(board, row, even, disc)
            if max_score < current_score:
                max_score = current_score
                best_columns = []
                best_columns.append(even)
            elif max_score == current_score:
                best_columns.append(even)
            board[row][even] = None
        if not evens:
            best_columns = columns
        best_column = self.rand_provider.prob_choice(best_columns, None)
        return best_column

    def odd_column(self, board, columns, disc):
        odds = []
        for i in columns:
            if i % 2 == 1:
                odds.append(i)
        max_score = 0
        best_columns = []
        for odd in odds:
            row = self.checker.simulate_play(board, odd)
            current_score = self.__calculate_score(board, row, odd, disc)
            if max_score < current_score:
                max_score = current_score
                best_columns = []
                best_columns.append(odd)
            elif max_score == current_score:
                best_columns.append(odd)
            board[row][odd] = None
        if not odds:
            best_columns = columns
        best_column = self.rand_provider.prob_choice(best_columns, None)
        return best_column

    def even_column(self, board, columns, disc):
        evens = []
        for i in columns:
            if i % 2 == 0:
                evens.append(i)
        max_score = 0
        best_columns = []
        for even in evens:
            row = self.checker.simulate_play(board, even)
            current_score = self.__calculate_score(board, row, even, disc)
            if max_score < current_score:
                max_score = current_score
                best_columns = []
                best_columns.append(even)
            elif max_score == current_score:
                best_columns.append(even)
            board[row][even] = None
        if not evens:
            best_columns = columns
        best_column = self.rand_provider.prob_choice(best_columns, None)
        return best_column

    def __calculate_score(self, board, row, column, disc):
        horizontal = self.searcher.search_horizontal(board, row, column)
        vertical = self.searcher.search_vertical(board, row, column)
        negative_diagonal = self.searcher.search_negative_diagonal(
            board, row, column)
        positive_diagonal = self.searcher.search_positive_diagonal(
            board, row, column)

        score = (self.score.score_combinations(horizontal, disc)
                 + self.score.score_combinations(negative_diagonal, disc)
                 + self.score.score_combinations(positive_diagonal, disc)
                 + self.score.score_combinations(vertical, disc))
        return score
