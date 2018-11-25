from abc import ABCMeta, abstractmethod

class GameAgent(metaclass=ABCMeta):
    
    @property
    def disc(self):
        try:
            return self._disc
        except AttributeError:
            raise NotImplementedError(
                "Subclasses of GameAgent must set an instance attribute ")

    @abstractmethod
    def play(self, board, columns):
        pass

    @disc.setter
    def disc(self, disc):
        self._disc = disc