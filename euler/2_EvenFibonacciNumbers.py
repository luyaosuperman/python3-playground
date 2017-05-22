#!/usr/bin/python3
import unittest

class Solution(unittest.TestCase):


	def sol(self):
		self.result = 0
		self.count  = 0

		self.a = 1
		self.b = 2
		self.result = 0

		while self.a < 4000000:
			if (self.count - 1) % 3 == 0:
				print(self.a)
				self.result += self.a
			self.feb()
		print(self.result)


	def feb(self):
		self.b, self.a = self.a + self.b, self.b
		self.count += 1



	def test_1(self):
		#self.assertEqual()
		self.sol()




if __name__ == '__main__':
    unittest.main()