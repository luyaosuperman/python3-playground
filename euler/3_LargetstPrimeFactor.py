#!/usr/bin/python3
import unittest

class Solution(unittest.TestCase):

	def sol(self):
		self.target = 600851475143
		self.candidates = []
		for i in range(2,self.target):
			if self.target % i == 0:
				print(i, self.target / i)
				self.candidates.append(i)
			if  i > self.target / i:
				break

		self.candidates = reversed(self.candidates)
		for candidate in self.candidates:
			print("testing", candidate)
			for i in range(2, int((candidate+1)/2)):
				if candidate % i == 0:
					print("divide by", i)
					break
			if i == int((candidate+1)/2) - 1 :
				print("largest prime", candidate)
				break



	def test_1(self):
		#self.assertEqual()
		self.sol()

if __name__ == '__main__':
    unittest.main()