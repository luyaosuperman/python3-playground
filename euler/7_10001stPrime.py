#!/usr/bin/python3
import unittest

class Solution(unittest.TestCase):

	def sol(self):
		count = 4
		i=9

		while count <= 10001:
			i += 2
			if self.primeTest(i):
				count += 1
				print("{0}th : {1}".format(count, i))


	def primeTest(self, n):
		for i in range(2, int((n ** 0.5) + 1)):
			if n % i == 0:
				return False
		return True


	def test_1(self):
		#self.assertEqual(			)
		self.sol()

if __name__ == '__main__':
    unittest.main()