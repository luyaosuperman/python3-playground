

class Veichle(metaclass=ABCMeta):
    def __init__(self):
        self.lot = None

    @abstractmethod
    def getVeichleSize(self):
        pass

    def park(self, lot):
        assert(self.lot == None)
        self.lot = lot

    def retrive(self):
        assert(self.lot != None)
        result = self.lot
        self.lot = None
        return result

class SmallVeichle(Veichle):
    def __init__(self):
        super.__init__()

    def getVeichleSize(self):
        return 0

#class MediumVeichle(Veichle):
#   pass

class LargeVeichle(Veichle):
    def __init__(self):
        super.__init__()

    def getVeichleSize(self):
        return 1

##########################################
class Lot(metaclass=ABCMeta):

    def __init__(self):
        self.veichle = None

    @abstractmethod
    def getLotSize(self):
        pass

    def park(self, veichle):
        assert(self.veichle == None)
        self.veichle = veichle

    def retrive(self):
        assert(self.veichle != None)
        result = self.veichle
        self.veichle = None
        return result

class LargeLot(Lot):
    def __init__(self):
        super.__init__()

    def getLotSize(self):
        return 1

#class MediumLot(Lot):
    #pass

class SmallLot(Lot):
    def __init__(self):
        super.__init__()

    def getLotSize(self):
        return 2

##########################################
class CarparkManager():

    def __init__(self, numberOfSmall, numberOfLarge):
        #init the carpark list

        self.smallLotList = []
        self.largeLotList = []

        self.numberOfSmall = numberOfSmall
        self.numberOfLarge = numberOfLarge

        self.smallOccupied = 0
        self.largeOccupied = 0

    def Park(self, veichle):
        assert(veichle.lot == None)
        park = None
        if veichle.getVeichleSize == 1 :
            #park a small veichle
            if self.smallOccupied < self.numberOfSmall:
            #in a small lot
                park = SmallLot()

            elif self.largeOccupied < self.numberOfLarge:
            #in a large lot
                park = LargeLot()

        elif veichle.getVeichleSize == 2 
            if self.largeOccupied < self.numberOfLarge:
            #park a large veichle
            park = LargeLot()

        if park != None:
            park.park(veichle)
            veichle.park(park)
            if park.getLotSize() == 1:
                self.smallLotList.append(park)
                self.smallOccupied += 1
            elif park.getLotSize() == 2:
                self.largeLotList.append(park)
                self.largeOccupied += 1
        else:
            raise RuntimeError("Carpark full!!!")




    def fetch(self, veichle):
        assert(veichle.lot != None)
        assert(veichle.lot.veichle == veichle)
        park = veichle.retrive()
        park.retrive()
        if park.getLotSize() == 1:
            self.smallLotList.remove(park)
            self.smallOccupied -= 1
            assert(self.smallOccupied >= 0)
        elif park.getLotSize() == 2:
            self.largeLotList.remove(park)
            self.largeOccupied -= 1
            assert(self.largeOccupied >= 0)


    def pushDown(self):
        pass




