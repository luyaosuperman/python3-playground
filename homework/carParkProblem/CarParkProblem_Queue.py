import unittest
import random
import threading
import time
from car import *
from lot import *


class CarparkManager():

    def __init__(self, numberOfSmall, numberOfLarge):
        #init the carpark list

        self.smallLotList = []
        self.largeLotList = []

        self.numberOfSmall = numberOfSmall
        self.numberOfLarge = numberOfLarge

        self.smallOccupied = 0
        self.largeOccupied = 0

    def park(self, car):
        print("--------")
        assert(car.lot == None)
        
        park = self.retriveLot(car)

        if park != None:
            park.park(car)
            car.park(park)
            if park.getLotSize() == 1:
                self.smallLotList.append(park)
                self.smallOccupied += 1
            elif park.getLotSize() == 2:
                self.largeLotList.append(park)
                self.largeOccupied += 1
            else:
                raise RuntimeError("Should not arrive here")
        else:
            raise RuntimeError("Carpark full!!!")

        self.trace()


    def retriveLot(self, car):
        park = None
        if car.getCarSize() == 1 :
            #park a small car
            if self.smallOccupied <= self.numberOfSmall:
            #in a small lot
                print("small car -> small lot")
                park = SmallLot()

            elif self.largeOccupied <= self.numberOfLarge:
            #in a large lot
                print("small car -> large lot")
                park = LargeLot()
            else:
                raise RuntimeError("Should not arrive here")

        elif car.getCarSize() == 2:
            if self.largeOccupied <= self.numberOfLarge:
                #park a large car
                print("large car -> large lot")
                park = LargeLot()
        else:
            raise RuntimeError("Should not arrive here")

        return park

    def fetch(self, car):
        print("========")
        assert(car.lot != None)
        assert(car.lot.car == car)
        park = car.retrive()
        park.retrive()
        if park.getLotSize() == 1:
            self.smallLotList.remove(park)
            self.smallOccupied -= 1
            assert(self.smallOccupied >= 0)
        elif park.getLotSize() == 2:
            self.largeLotList.remove(park)
            self.largeOccupied -= 1
            assert(self.largeOccupied >= 0)

        self.trace()


    def pushDown(self):
        pass

    def trace(self):
        print("small cars parked:", self.smallOccupied, "out of", self.numberOfSmall)
        for park in self.smallLotList:
            print(park.getLotId(), "->", park.car.getCarId(), end = ", ")
        print()

        print("large cars parked:", self.largeOccupied, "out of", self.numberOfLarge)
        for park in self.largeLotList:
            print(park.getLotId(), "->", park.car.getCarId(), end = ", ")
        print()


#class CarManager():
    #manage a pool of cars
    #manage creating multiple park and fetch request



class Test(unittest.TestCase):


    def parkACar(self, car):
        self.carparkManager.park(car)

    def fetchACar(self, car):
        self.carparkManager.fetch(car)

    def test_1(self):
        self.carparkManager = CarparkManager(10,10)
        smallCars = []
        largeCars = []
        for i in range(10):
            smallCars.append(SmallCar())
            largeCars.append(LargeCar())


        for i in range(10):
            #print("\nparking small", smallCars[i].getCarId())
            #self.carparkManager.park(smallCars[i])

            #print("\nparking large", largeCars[i].getCarId())
            #self.carparkManager.park(largeCars[i])
            threading.Thread(target = self.parkACar, args = (smallCars[i],)).start()
            threading.Thread(target = self.parkACar, args = (largeCars[i],)).start()


        time.sleep(1)

        for i in range(10):
            #print("\nfetching small", smallCars[i].getCarId())
            #self.carparkManager.fetch(smallCars[i])

            #print("\nfetching small", smallCars[i].getCarId())
            #self.carparkManager.fetch(largeCars[i])
            threading.Thread(target = self.fetchACar, args = (smallCars[i],)).start()
            threading.Thread(target = self.fetchACar, args = (largeCars[i],)).start()




if __name__ == '__main__':
    random.seed(1)
    unittest.main()


