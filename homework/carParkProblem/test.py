from CarParkProblem import CarparkManager
import unittest
from car import *
from lot import *


class Test(unittest.TestCase):

    def testFillAndThenEmpty(self):
        """Fill a car park, and then empty it"""
        carparkManager = CarparkManager(10, 10)
        smallCars = []
        largeCars = []
        for i in range(10):
            smallCars.append(SmallCar())
            largeCars.append(LargeCar())

        for i in range(10):
            #print("\nparking small", smallCars[i].getCarId())
            carparkManager.park(smallCars[i])

            #print("\nparking large", largeCars[i].getCarId())
            carparkManager.park(largeCars[i])

        # Test out if every car is parked
        for i in range(10):
            self.assertNotEqual(smallCars[i].lot, None)
            self.assertNotEqual(largeCars[i].lot, None)

        # Test out if the number of cars in the carpark is correct
        self.assertEqual(carparkManager.smallOccupied, 10)
        self.assertEqual(carparkManager.largeOccupied, 10)

        # No parking lot
        self.assertRaises(RuntimeError, carparkManager.park, SmallCar())
        self.assertRaises(RuntimeError, carparkManager.park, LargeCar())

        for i in range(10):
            #print("\nfetching small", smallCars[i].getCarId())
            carparkManager.fetch(smallCars[i])

            #print("\nfetching small", smallCars[i].getCarId())
            carparkManager.fetch(largeCars[i])

        # Test out if every car is retrieved
        for i in range(10):
            self.assertEqual(smallCars[i].lot, None)
            self.assertEqual(largeCars[i].lot, None)

        self.assertEqual(len(carparkManager.smallLotList), 0)
        self.assertEqual(len(carparkManager.largeLotList), 0)

    def testPushDown(self):
        carparkManager = CarparkManager(10, 10)
        smallCars = []
        largeCars = []
        for i in range(20):
            smallCars.append(SmallCar())

        # Park first 10 small cars, they should end up in small carpark
        for i in range(10):
            carparkManager.park(smallCars[i])

        for i in range(10):
            self.assertNotEqual(smallCars[i].lot, None)

        for i in range(10, 20):
            self.assertEqual(smallCars[i].lot, None)

        self.assertEqual(carparkManager.smallOccupied, 10)
        self.assertEqual(carparkManager.largeOccupied, 0)


        # Park next 10 small cars, they should end up in large carpark
        for i in range(10, 20):
            carparkManager.park(smallCars[i])

        for i in range(10, 20):
            self.assertNotEqual(smallCars[i].lot, None)

        self.assertEqual(carparkManager.smallOccupied, 10)
        self.assertEqual(carparkManager.largeOccupied, 10)

        # fetch cars from small carpark first, 
        # then cars stay in large carpark should moves to small carpark
        for i in range(10):
            carparkManager.fetch(smallCars[i])

        self.assertEqual(carparkManager.smallOccupied, 10)
        self.assertEqual(carparkManager.largeOccupied, 0)


if __name__ == '__main__':
    unittest.main()
