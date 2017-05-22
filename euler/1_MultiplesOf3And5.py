#!/usr/bin/python3
import unittest

class Solution(unittest.TestCase):

    def sol(self,n):
        result = 0
        for i in range(n):
            if i % 3 == 0 or i % 5 == 0:
                result += i

        return result


    def test_1(self):
        self.assertEqual(
                self.sol(10), 23
            )
        print(self.sol(1000))

if __name__ == '__main__':
    unittest.main()