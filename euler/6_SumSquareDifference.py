#!/usr/bin/python3
import unittest

class Solution(unittest.TestCase):

	def sol(self, n):
		result = 0
		for i in range(1, n+1):
			for j in range(i+1, n+1):
				result += i*j*2
		print(result)


	def test_1(self):
		#self.assertEqual(

		#	)
		self.sol(10)
		self.sol(100)

if __name__ == '__main__':
    unittest.main()