from abc import ABCMeta
from abc import abstractmethod
import random


class Car(metaclass=ABCMeta):
    '''
    abstract car class
    '''
    SMALL = 1
    LARGE = 2

    def __init__(self):
        self.lot = None
        self.id = random.randrange(100)

    @abstractmethod
    def getCarSize(self):
        '''
        what kind of car it is.
        '''
        raise RuntimeError("Not implemented")

    def getCarId(self):
        '''
        Unique ID of the car. For identification purpose
        '''
        return self.id

    def park(self, lot):
        '''
        Store the information of parking lot 
        inside the car as well
        '''
        assert(self.lot == None)
        self.lot = lot

    def retrieve(self):
        '''
        remove carpark information from the car
        once it is taken out
        '''
        assert(self.lot != None)
        result = self.lot
        self.lot = None
        return result


class SmallCar(Car):
    """
    implementation of a small car
    """
    def __init__(self):
        super().__init__()

    def getCarSize(self):
        return Car.SMALL

#class MediumCar(Car):
#   pass


class LargeCar(Car):
    """
    implementation of a large car
    """
    def __init__(self):
        super().__init__()

    def getCarSize(self):
        return Car.LARGE