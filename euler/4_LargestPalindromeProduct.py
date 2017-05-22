#!/usr/bin/python3
import unittest
from functools import reduce

class Solution(unittest.TestCase):

	def sol(self):
		#999 * 999 = 998001
		for i in range(999,99,-1): # 998 -> 100
			target = i * 1000 + int(int("".join(reversed(str(i)))))
			print("target", target)
			maxF = self.maxFactor(target)
			print("attemping", maxF)
			if ( target // maxF >= 100):
				print("divident", maxF, target // maxF)
				break



	def maxFactor(self, n):
		resultSet = self.factors(n)
		if len(resultSet) == 0:
			return n
		else:
			return max(resultSet)

	def factors(self,n):
		return set(
				reduce(
					list.__add__,
					#([i, n//i] for i in range(2, int(n**0.5) + 1) \
					([i, n//i] for i in range(100, 999 + 1) \
						if n % i == 0 and \
						i >= 100 and n//i >= 100 and\
						i < 1000 and n//i < 1000
						),
					[]
					)
			)


	def test_1(self):
		self.sol()

if __name__ == '__main__':
    unittest.main()