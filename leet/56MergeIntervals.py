import unittest

debugPrint = False  # only print if it is True
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

# Definition for an interval.


class Interval(object):

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(unittest.TestCase):

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        self.intervals = intervals
        self.sort()
        return self.intervals

    def sort(self):
        N = len(self.intervals)
        sz = 1
        while sz < N:
            lo = 0
            while lo < N - sz:
                lastRound = (sz * 2 >= N)
                self.__merge(lo, lo + sz - 1,
                             min(lo + 2 * sz - 1, N - 1), lastRound)
                lo += sz * 2
            sz *= 2

    #@printStack
    def __merge(self, lo, mid, hi, lastRound):
        xPrint("lastRound:", lastRound)
        lows = []
        highs = []
        xPrint("range(mid, lo - 1, -1)",
               range(mid, lo - 1, -1),
               list(range(mid, lo - 1, -1)),
               )
        for i in range(mid, lo - 1, -1):  # [lo, mid]
            # for i in range(lo, mid + 1, -1):  # [lo, mid]
            lows.append(self.intervals[i])  # stack

        # for i in range(mid + 1, hi + 1, -1):  # [mid+1, hi]
        xPrint("range(hi, mid, -1)",
               range(hi, mid, -1),
               list(range(hi, mid, -1)),
               )
        for i in range(hi, mid, -1):  # [mid+1, hi]
            highs.append(self.intervals[i])  # stack

        xPrint("lows")
        for item in lows:
            xPrint("-- l: %s h: %s" % (item.start, item.end))
        for item in highs:
            xPrint("++ l: %s h: %s" % (item.start, item.end))
        #xPrint("highs", highs)
        cursor = lo

        if lastRound:
            self.intervals = list()
        while len(lows) + len(highs) > 0:

            if len(lows) == 0:
                if not lastRound:
                    self.intervals[cursor] = highs.pop()
                    cursor += 1
                else:
                    self.intervals.append(highs.pop())
                    self.__mergeNeighbor(lastRound)
                continue
            if len(highs) == 0:
                if not lastRound:
                    self.intervals[cursor] = lows.pop()
                    cursor += 1
                else:
                    self.intervals.append(lows.pop())
                    self.__mergeNeighbor(lastRound)
                continue

            if self.less(lows[-1], highs[-1]):
                if not lastRound:
                    self.intervals[cursor] = lows.pop()
                    cursor += 1
                else:
                    self.intervals.append(lows.pop())
                    self.__mergeNeighbor(lastRound)
            else:
                if not lastRound:
                    self.intervals[cursor] = highs.pop()
                    cursor += 1
                else:
                    self.intervals.append(highs.pop())
                    self.__mergeNeighbor(lastRound)

            

    def __mergeNeighbor(self, lastRound):
        if lastRound == True and len(self.intervals) > 1:
            xPrint("Try merging")
            item0 = self.intervals[-2]
            item1 = self.intervals[-1]
            xPrint("testing %s.%s and %s.%s" %
                       (item0.start, item0.end,
                        item1.start, item1.end)
                       )
            if item0.end >= item1.start:
                xPrint("merge %s.%s and %s.%s" %
                       (item0.start, item0.end,
                        item1.start, item1.end)
                       )
                item0.end = max(item0.end, item1.end)
                self.intervals.pop()
                return -1
        return 0

    #@printStack
    def less(self, interval1, interval2):
        # return true if interval1.start < interval2.start
        assert(interval1 != None)
        assert(interval2 != None)
        return interval1.start < interval2.start

    '''@printStack
    def exch(self, items, i, j):
        # exchange items in place i and j
        assert(0 < i)
        assert(0 < j)
        assert(i < len(items) - 1)
        assert(j < len(items) - 1)
        temp = items[i]
        items[i] = items[j]
        items[j] = temp'''

    def test_1(self):
        inputs = [
            [1, 3], [2, 6], [8, 10], [15, 18]
        ]

        outputs = [[1, 6], [8, 10], [15, 18]]
        self.actual_test(inputs, None)

    def test_2(self):
        inputs = [
            [8, 10], [15, 18], [1, 3], [2, 6],
        ]

        outputs = [[1, 6], [8, 10], [15, 18]]
        self.actual_test(inputs, None)

    def test_3(self):
        inputs = [
            [8, 10], [1, 3], [15, 18],  [2, 6],
        ]

        outputs = [[1, 6], [8, 10], [15, 18]]
        self.actual_test(inputs, None)

    def actual_test(self, inputs, outputs):
        __input = []
        for item in inputs:
            __input.append(Interval(item[0], item[1]))
        for item in __input:
            print("i --> l: %s h: %s" % (item.start, item.end))
        __output = self.merge(__input)
        for item in __output:
            print("o <-- l: %s h: %s" % (item.start, item.end))

        print("=============")
        # for i in range(len(outputs)):
        #    self.assertEqual(self.numIslands(inputs[i]), outputs[i])


if __name__ == '__main__':
    unittest.main()
