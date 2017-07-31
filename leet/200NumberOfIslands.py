import unittest

debugPrint = False  # only print if it is True
stackPrint = False


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

    @printStack
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.grid = grid

        self.rows = len(self.grid)
        if self.rows == 0:
            return 0

        self.cols = len(self.grid[0])
        if self.cols == 0:
            return 0

        self.init()
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == '1':
                    pairs = self.findPairs(i,j)
                    for pair in pairs:
                        self.union(i,j,pair[0],pair[1])

        return self.count

    @printStack
    def init(self):
        self.count = 0
        self.id = []
        self.sz = []
        for i in range(self.rows):
            self.sz.append([1] * self.cols)
            self.id.append([0] * self.cols)
            for j in range(self.cols):
                if self.grid[i][j] == '1':
                    self.count += 1
                    self.id[i][j] = self.getId(i,j)

        xPrint("self.count:", self.count)

    #def count(self):
    #    return self.count

    #@printStack
    def getId(self, row, col):
        return row * self.cols + col

    #@printStack
    def getRowCol(self, i):
        row = i // self.cols
        col = i % self.cols
        return [row, col]

    @printStack
    def union(self, row1, col1, row2, col2):
        i1 = self.find(row1, col1)
        i2 = self.find(row2, col2)
        if i1 != i2:
            xPrint("%s.%s has different parent with %s.%s" % (row1, col1, row2, col2))
            #self.id[row1][col1] = i2
            rootRow, rootCol = self.getRowCol(i1)
            self.id[rootRow][rootCol] = i2
            self.count -= 1
            xPrint("self.count:", self.count)
        else:
            xPrint("%s.%s has same parent with %s.%s" % (row1, col1, row2, col2))
            pass
        for id_ in self.id:
            xPrint(id_)

    @printStack
    def find(self, row, col):
        while self.id[row][col] != self.getId(row, col):
            row, col = self.getRowCol(self.id[row][col])
        assert(self.id[row][col] == self.getId(row, col))
        return self.id[row][col]

    #def connected(self, row1, col1, row2, col2):
    #    pass
    @printStack
    def findPairs(self, row, col):
        results  = []
        if row < self.rows-1 and self.grid[row+1][col] == '1':
            results.append([row+1, col])
        if col < self.cols-1 and self.grid[row][col+1] == '1':
            results.append([row, col+1])

        return results

    def test_1(self):
        inputs = [
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
        ]

        outputs = [1,]
        for i in range(len(outputs)):
            self.assertEqual(self.numIslands(inputs[i]), outputs[i])


    def test_2(self):
        inputs = [
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
        ]

        outputs = [3]
        for i in range(len(outputs)):
            self.assertEqual(self.numIslands(inputs[i]), outputs[i])
if __name__ == '__main__':
    unittest.main()