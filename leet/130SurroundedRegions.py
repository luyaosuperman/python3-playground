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

    @printStack
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.

        The idea:
        Find one from the edge,
        mark it as Z,
        continue to mark its neighbor as Z
        Do it for all O from the edge.

        Then, flip all remaining O to X
        and flip all Z to O
        """
        self.lenX = len(board)
        if self.lenX == 0:
            return
        self.lenY = len(board[0])

        self.board = board

        self.getOList()

        for cord in self.OList:
            x = cord[0]
            y = cord[1]
            if self.board[x][y] == "O":
                self.findAllNeighbors(cord)

        self.cleanUp()

    @printStack
    def getOList(self):
        self.OList = []  # a list of tuple of (x, y) cord
        for x in range(self.lenX):
            for y in [0, self.lenY - 1]:
                if self.board[x][y] == "O":
                    xPrint("Found O at %s %s" % (x, y))
                    self.OList.append((x, y))

        for y in range(1, self.lenY - 1):
            # not form 0 to remove duplicate
            for x in [0, self.lenX - 1]:
                if self.board[x][y] == "O":  # if it is still O
                    xPrint("Found O at %s %s" % (x, y))
                    self.OList.append((x, y))

    @printStack
    def findAllNeighbors(self, cord):
        """
        flip all neighbor O to Z
        """
        #visited = [[False] * self.lenY] * self.lenX
        stack = []
        stack.append(cord)

        while len(stack) > 0:
            currentCord = stack.pop()
            currentX = currentCord[0]
            currentY = currentCord[1]
            #visited[currentX][currentY] = True
            self.board[currentX][currentY] = "Z"
            neighborCordList = self.findNeighborOfCell(currentCord)
            for neighborCord in neighborCordList:
                stack.append(neighborCord)

    @printStack
    def findNeighborOfCell(self, cord):
        result = []
        x = cord[0]
        y = cord[1]

        # 1 left
        if x > 0 and self.board[x - 1][y] == "O":
            result.append((x - 1, y))

        # 2 up
        if y > 0 and self.board[x][y - 1] == "O":
            result.append((x, y - 1))
        # 3 right
        if x < self.lenX - 1 and self.board[x + 1][y] == "O":
            result.append((x + 1, y))
        # 4 down
        if y < self.lenY - 1 and self.board[x][y + 1] == "O":
            result.append((x, y + 1))

        return result

    @printStack
    def cleanUp(self):
        for x in range(self.lenX):
            for y in range(self.lenY):
                if self.board[x][y] == "O":
                    self.board[x][y] = "X"
                elif self.board[x][y] == "Z":
                    self.board[x][y] = "O"


class Test(unittest.TestCase):

    def test1(self):
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]

        result = [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "O", "X", "X"],
        ]
        sol = Solution()
        sol.solve(board)
        xPrint(board)
        for x in range(len(board)):
            self.assertListEqual(board[x], result[x])

    def test2(self):
        board = [
            ["X", "X", "X", "X"],
            ["X", "X", "O", "X"],
            ["O", "O", "X", "X"],
            ["X", "O", "X", "X"],
        ]

        result = [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["O", "O", "X", "X"],
            ["X", "O", "X", "X"],
        ]
        sol = Solution()
        sol.solve(board)
        xPrint(board)
        for x in range(len(board)):
            self.assertListEqual(board[x], result[x])

if __name__ == '__main__':
    unittest.main()
