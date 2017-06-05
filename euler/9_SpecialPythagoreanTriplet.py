#!/usr/bin/python3
import unittest

class Solution(unittest.TestCase):

	def sol(self):
		for a in range(1,334+1):
			for b in range(a, (1000-a)//2 + 1):
				c = 1000 - a - b
				if a*a + b*b == c*c:
					print("{0} {1} {2} -> {3} {4}".format(a,b,c, a*a + b*b, c*c ))
					print(a*b*c)
					return a*b*c


	def test_1(self):
		#self.assertEqual(			)
		self.sol()

if __name__ == '__main__':
    unittest.main()