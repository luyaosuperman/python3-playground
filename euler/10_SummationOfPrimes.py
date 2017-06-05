#!/usr/bin/python3
import unittest

class Solution(unittest.TestCase):

	def sol(self):
		result = 0
		for i in range(2,2000000+1):
			if i % 10000 == 0:
				print(i)
			if self.primeTest(i):
				#print(i, end=' ')
				result += i
		print("result ", result)


	def primeTest(self, n):
		if n == 2:
			return True
		for i in range(2, int((n ** 0.5) + 1)):
			if n % i == 0:
				return False
		return True


	def test_1(self):
		#self.assertEqual(			)
		self.sol()

if __name__ == '__main__':
    unittest.main()