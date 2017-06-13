from abc import ABCMeta
from abc import abstractmethod
import random

class Lot(metaclass=ABCMeta):
    """
    parking lot class
    """

    SMALL = 1
    LARGE = 2

    def __init__(self):
        self.car = None
        self.id = random.randrange(100)

    @abstractmethod
    def getLotSize(self):
        pass

    def getLotId(self):
        """
        Lot id, for debug purpose
        """
        return self.id

    def park(self, car):
        """
        park a car in the lot
        """
        assert(self.car == None)
        self.car = car

    def retrieve(self):
        """
        fetch a car in the log
        """
        assert(self.car != None)
        result = self.car
        self.car = None
        return result

class SmallLot(Lot):
    """
    Implementation of small lot
    """
    def __init__(self):
        super().__init__()

    def getLotSize(self):
        return Lot.SMALL

#class MediumLot(Lot):
    #pass

class LargeLot(Lot):
    """
    Implementation of large lot
    """
    def __init__(self):
        super().__init__()

    def getLotSize(self):
        return Lot.LARGE


