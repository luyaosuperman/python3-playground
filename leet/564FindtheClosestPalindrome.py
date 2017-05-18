#!/bin/python3.6
import unittest

class Solution(unittest.TestCase):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """

        l = len(n)
        if l == 1:
            return str(int(n) - 1)

        candidates = set(( ( "1"+"0"*(l-1)+"1" ), "9"*(l-1) ))
        prefix = int( n[:int((l+1)/2)] )

        for i in map(str, (prefix -1, prefix, prefix + 1)):
            candidates.add(i+[i,i[:-1]][l & 1][::-1])
            print(i, i+[i,i[:-1]][l & 1][::-1])
        print(candidates)
        candidates.discard(n)

        return min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))


    def test_1(self): #corner case
        inputNumbers  = ['121', '1', '10']
        outputNumbers = ['111', '0', '9' ]

        for inputNumber, outputNumber in zip(inputNumbers, outputNumbers):
            self.assertEqual(self.nearestPalindromic(inputNumber), outputNumber)



if __name__ == '__main__':
    unittest.main()
