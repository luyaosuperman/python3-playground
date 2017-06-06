import unittest
#from string import ascii_lowercase
import string

class Solution(unittest.TestCase):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        result = 0
        sums = []
        for i in nums:
            result += i
            sums.append(result)
        print(sums)

'''
assume j < i
lower         <= sum[i] - sum[j]  <= upper
-upper        <= sum[j] - sum[i]  <= -lower
sum[i] -upper <= sum[j]           <= sum[i] - lower
'''


    def test_1(self):
        #self.assertEqual()
        nums = [-2, 5, -1]
        lower = -2
        upper = 2

        self.countRangeSum(nums,lower,upper)

if __name__ == '__main__':
    unittest.main()