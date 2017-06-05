#!/usr/bin/python3
from abc import ABCMeta
from abc import abstractmethod
import unittest
from unittest.mock import patch
#from mock import Mock
import drinks

class MyABC(metaclass=ABCMeta):
	pass

MyABC.register(tuple)
assert issubclass(tuple, MyABC)
assert isinstance((), MyABC)
print("issubclass(tuple, MyABC)", issubclass(tuple, MyABC))
print("isinstance((), MyABC)", isinstance((), MyABC))

#class Drink(object):
#class Coke(Drink):

class Foo:
	def __getitem__(self,index):
		pass

	def __len__(self):
		pass

	def get_iterator(self):
		return iter(self)

class MyIterable(metaclass=ABCMeta):

	@abstractmethod
	def __titer__(self):
		while False:
			yield None

	def get_iterator(self):
		return self.__iter__()

	@classmethod
	def __subclasshook__(cls, C):
		if cls is MyIterable:
			if any("__iter__" in B.__dict__ for B in C.__mro__):
				return True
			return NotImplemented

MyIterable.register(Foo)



class Base(metaclass=ABCMeta):
	@abstractmethod
	def foo(self):
		pass

	@abstractmethod
	def bar(self):
		pass

class Concrete(Base):
	def foo(self):
		pass

#c = Concrete()
'''
Traceback (most recent call last):
  File "./classPractice.py", line 61, in <module>
    c = Concrete()
TypeError: Can't instantiate abstract class Concrete with abstract methods bar
'''

class Test(unittest.TestCase):


	def getDrink(self):
		if drinks.Drink.isFriday():
			return drinks.Beer()
		else:
			return drinks.CocaCola()


	@patch('drinks.Drink.isFriday', return_value=False)
	def test_1(self, *args, **keywargs):
		print("drinks.Drink.isFriday():", drinks.Drink.isFriday())

		returnObj = self.getDrink()
		self.assertEqual(returnObj.getName(),"CocaCola")

	def test_2(self, *args, **keywargs):
		returnVal = unittest.mock.Mock(return_value=False)
		drinks.Drink.isFriday = returnVal
		print("drinks.Drink.isFriday():", drinks.Drink.isFriday())

		returnObj = self.getDrink()
		self.assertEqual(returnObj.getName(),"CocaCola")

'''@patch("Drink.isFriday")
def isFridayMock():
	return False'''


if __name__ == "__main__":
	coke = drinks.CocaCola()
	print(coke.getName())
	print(coke.getBestTemperature())

	beer = drinks.Beer()
	print(beer.getName())
	print(beer.getDegree())

	unittest.main()

