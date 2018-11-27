from abc import ABCMeta, abstractmethod


class Chromosome(metaclass=ABCMeta):

    @abstractmethod
    def mutate(self):
        pass

    @abstractmethod
    def cross(self, chromosome):
        pass
