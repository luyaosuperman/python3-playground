import unittest

class Solution(unittest.TestCase):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[::2])

    def test_1(self):
    	inputs = [1,4,3,2]
    	outputs = 4
    	self.assertEqual(self.arrayPairSum(inputs), outputs)


if __name__ == '__main__':
	unittest.main()