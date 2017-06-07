from abc import ABCMeta
from abc import abstractmethod
import random

class Car(metaclass=ABCMeta):
    def __init__(self):
        self.lot = None
        self.id = random.randrange(100)

    @abstractmethod
    def getCarSize(self):
        pass

    def getCarId(self):
        return self.id

    def park(self, lot):
        assert(self.lot == None)
        self.lot = lot

    def retrive(self):
        assert(self.lot != None)
        result = self.lot
        self.lot = None
        return result

class SmallCar(Car):
    def __init__(self):
        super().__init__()

    def getCarSize(self):
        return 1

#class MediumCar(Car):
#   pass

class LargeCar(Car):
    def __init__(self):
        super().__init__()

    def getCarSize(self):
        return 2