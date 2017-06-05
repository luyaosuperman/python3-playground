
from abc import ABCMeta
from abc import abstractmethod
#############################################
class Drink(metaclass=ABCMeta):
	@abstractmethod
	def getName(self):
		pass

	@abstractmethod
	def isAlcoholFree(self):
		pass

	@abstractmethod
	def isSoda(self):
		pass

	def isFriday():
		return True


class Soda(Drink, metaclass=ABCMeta):
	@abstractmethod
	def getBestTemperature(self):
		pass

	def isAlcoholFree(self):
		return True

	def isSoda(self):
		return True

class CocaCola(Soda):
	def getName(self):
		return "CocaCola"

	def getBestTemperature(self):
		return 4

###
class Alcohol(Drink, metaclass=ABCMeta):
	@abstractmethod
	def getDegree(self):
		pass

	def isAlcoholFree(self):
		return False

	def isSoda(self):
		return False

class Beer(Alcohol):
	def getName(self):
		return "beer"

	def getDegree(self):
		return 5