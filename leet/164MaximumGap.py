import unittest

debugPrint = True  # only print if it is True
stackPrint = True


def xPrint(*args):
    """
    A print function that can be turned on/off
    """
    if debugPrint:
        print(*args)


def printStack(method):
    """
    print the name of the method
    """
    def printed(*args, **kw):
        if stackPrint:
            xPrint("++", method.__name__, args, kw)
        result = method(*args, **kw)
        if stackPrint:
            xPrint("--", method.__name__, args, kw, "Returns", result)
        return result
    return printed


class Solution(unittest.TestCase):

    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 1:
            return 0

        gap = 0
        self.N = len(nums)
        self.nums = [0] + nums
        xPrint(self.nums)
        k = self.N // 2 
        while k >= 1:
            self.sink(k, self.N)
            k -= 1
            xPrint(self.nums)
        xPrint("-----phase 1 done")
        while(self.N >= 1):
            self.exch(1, self.N)
            xPrint(self.nums, self.N)
            if self.N < len(nums) :
                xPrint("gap:",self.nums[self.N+1] - self.nums[self.N])
                gap = max(gap, self.nums[self.N+1] - self.nums[self.N])
            self.N -= 1
            self.sink(1, self.N)
            

        return gap

    def sink(self, k, N):
        xPrint("sinking k:%s N:%s" % (k, N))
        while 2 * k <= N:
            j = 2 * k
            if j < N and self.nums[j] < self.nums[j + 1]:
                j += 1
            if self.nums[j] < self.nums[k]:
                break
            self.exch(k, j)
            k = j

    def exch(self, i, j):
        # exchange items in place i and j
        assert(0 < i)
        assert(0 < j)
        assert(i <= self.N)
        assert(j <= self.N)
        temp = self.nums[i]
        self.nums[i] = self.nums[j]
        self.nums[j] = temp

    def test_1(self):
        inputs = [5,4,3,2,1]
        outputs = 1
        self.actual_test(inputs, outputs)

    def test_2(self):
        inputs = [1,10000000]
        outputs = 9999999
        self.actual_test(inputs, outputs)

    def actual_test(self, inputs, outputs):

        print("=============")
        self.assertEqual(self.maximumGap(inputs), outputs)


if __name__ == '__main__':
    unittest.main()
