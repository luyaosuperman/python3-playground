import unittest

debugPrint = False  # only print if it is True
stackPrint = False


def xPrint(*args):
    """
    A print function that can be turned on/off
    """
    if debugPrint:
        print args


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

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2: #0,1
            return len(nums)

        numSet = set()
        #self.ids = list(range(max(nums) + 2))
        self.ids = dict()
        rootDict = dict()
        roots = list(range(len(nums)))

        for num in nums:
            if num not in numSet:
                numSet.add(num)
                self.ids[num] = num
                xPrint("working on num %s" % num)
                if num + 1 in numSet: #self.find(num, num+1): 
                    xPrint("find %s and %s" % (num, num+1))
                    self.unite(num, num+1)

                if num - 1 in numSet:#self.find(num, num-1):
                    xPrint("find %s and %s" % (num, num-1))
                    self.unite(num, num-1)
            else:
                #duplicate number
                pass

        """for i in range(len(nums)):
            roots[i] = self.root(nums[i])
            if roots[i] not in rootDict:
                rootDict[roots[i]] = 1
            else:
                rootDict[roots[i]] += 1"""

        i = 0
        for num in numSet:
            roots[i] = self.root(num)
            if roots[i] not in rootDict:
                rootDict[roots[i]] = 1
            else:
                rootDict[roots[i]] += 1
            i += 1

        maxCount = -1
        for root in rootDict:
            if rootDict[root] > maxCount:
                maxCount = rootDict[root]

        return maxCount

    def root(self, num):
        while num != self.ids[num]:
            num = self.ids[num]
        return num

    def unite(self, num1, num2):
        root1 = self.root(num1)
        root2 = self.root(num2)
        self.ids[root1] = root2

    def find(self, num1, num2):
        return self.root(num1) == self.root(num2)

class Test(unittest.TestCase):

    def test1(self):
        nums = [100, 4, 200, 1, 3, 2]
        expected = 4

        sol = Solution()
        self.assertEqual(sol.longestConsecutive(nums), expected)

    def test2(self):
        nums = [2147483646,-2147483647,0,2,2147483644,-2147483645,2147483645]
        sol = Solution()
        sol.longestConsecutive(nums)
        #self.assertEqual(sol.longestConsecutive(nums), expected)

        [100,4,200,1,3,2]

    def test3(self):
        nums = [100,4,200,1,3,2]
        sol = Solution()
        sol.longestConsecutive(nums)

    def test4(self):
        nums = [0,0]
        expected = 1
        sol = Solution()
        self.assertEqual(sol.longestConsecutive(nums), expected)

if __name__ == '__main__':
    unittest.main()
