from car import *
from lot import *


class CarparkManager():
    """
    This class will allocate carpark
    All park/fetch should be called by this class
    """

    def __init__(self, numberOfSmall, numberOfLarge):
        # init the carpark list

        self.smallLotList = []
        self.largeLotList = []

        self.numberOfSmall = numberOfSmall
        self.numberOfLarge = numberOfLarge

        self.smallOccupied = 0
        self.largeOccupied = 0

    def park(self, car):
        """
        park a car
        """
        #print("--------")
        assert(car.lot == None)

        park = self.retrieveLot(car)

        if park != None:
            park.park(car)
            car.park(park)
            if park.getLotSize() == Lot.SMALL:
                self.smallLotList.append(park)
                self.smallOccupied += 1
            elif park.getLotSize() == Lot.LARGE:
                self.largeLotList.append(park)
                self.largeOccupied += 1
            else:
                raise RuntimeError("Should not arrive here")
        else:
            raise RuntimeError("Carpark full!!!")

        #self.trace()

    def retrieveLot(self, car):
        """
        when park() is called, this function will find a lot for the car
        """
        park = None
        if car.getCarSize() == Car.SMALL:
            # park a small car
            if self.smallOccupied < self.numberOfSmall:
                # in a small lot
                #print("small car -> small lot")
                park = SmallLot()

            elif self.largeOccupied < self.numberOfLarge:
                # in a large lot
                #print("small car -> large lot")
                park = LargeLot()
            else:
                pass

        elif car.getCarSize() == Car.LARGE:
            if self.largeOccupied < self.numberOfLarge:
                # park a large car
                #print("large car -> large lot")
                park = LargeLot()
            else:
                pass
        else:
            raise RuntimeError("Should not arrive here")

        return park

    def fetch(self, car):
        """take out a car from the carpark"""
        #print("========")
        assert(car.lot != None)
        assert(car.lot.car == car)
        park = car.retrieve()
        park.retrieve()
        if park.getLotSize() == Lot.SMALL:
            self.smallLotList.remove(park)
            self.smallOccupied -= 1
            assert(self.smallOccupied >= 0)
        elif park.getLotSize() == Lot.LARGE:
            self.largeLotList.remove(park)
            self.largeOccupied -= 1
            assert(self.largeOccupied >= 0)

        #self.trace()

    def pushDown(self):
        """
        when a car is retrieved, 
        this function will optimize the carpark allocation by 
        moving around the existing cars.

        Not implmented
        """
        raise RuntimeError("Not Implemented")

    def trace(self):
        """
        print the carpark information for debug purpose
        """
        print("small cars parked:", self.smallOccupied,
              "out of", self.numberOfSmall)
        for park in self.smallLotList:
            print(park.getLotId(), "->", park.car.getCarId(), end=", ")
        print()

        print("large cars parked:", self.largeOccupied,
              "out of", self.numberOfLarge)
        for park in self.largeLotList:
            print(park.getLotId(), "->", park.car.getCarId(), end=", ")
        print()


