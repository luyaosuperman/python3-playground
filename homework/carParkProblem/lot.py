from abc import ABCMeta
from abc import abstractmethod
import random

class Lot(metaclass=ABCMeta):

    def __init__(self):
        self.car = None
        self.id = random.randrange(100)

    @abstractmethod
    def getLotSize(self):
        pass

    def getLotId(self):
        return self.id

    def park(self, car):
        assert(self.car == None)
        self.car = car

    def retrive(self):
        assert(self.car != None)
        result = self.car
        self.car = None
        return result

class LargeLot(Lot):
    def __init__(self):
        super().__init__()

    def getLotSize(self):
        return 1

#class MediumLot(Lot):
    #pass

class SmallLot(Lot):
    def __init__(self):
        super().__init__()

    def getLotSize(self):
        return 2