import graph
import unittest
import xprint


class SimpleGraphTest(unittest.TestCase):
    """
    Test out the function on an obvious graph
    """

    def setUp(self):
        """
        Setup an obvious graph
        """
        xprint.debugPrint = False
        self.testGraph = graph.UndirectionalGraph(6)
        self.testGraph.addEdge(0, 1, 2)
        self.testGraph.addEdge(1, 2, 3)
        self.testGraph.addEdge(0, 2, 1)
        self.testGraph.addEdge(2, 3, 5)
        self.testGraph.addEdge(3, 4, 5)
        self.testGraph.addEdge(3, 5, 7)
        self.testGraph.addEdge(4, 5, 3)

    def testHotLink(self):
        hotEdges = self.testGraph.findHotEdge()
        edgeCountExpects = {
            (0, 1): 2,
            (1, 2): 6,
            (2, 3): 14,
            (4, 5): 2,
            (3, 4): 6,
            (0, 2): 6,
            (3, 5): 6
        }

        for edge in edgeCountExpects:
            expect = edgeCountExpects[edge]
            self.assertEqual(hotEdges[edge], expect)