import graph
import unittest
import xprint


class DisconnectedGraphTest(unittest.TestCase):
    """
    Test out the function on an disconnected graph
    """

    def setUp(self):
        """
        Setup an disconnected graph
        """
        xprint.debugPrint = False
        self.testGraph = graph.UndirectionalGraph(6)
        self.testGraph.addEdge(0, 1, 2)
        self.testGraph.addEdge(1, 2, 3)
        self.testGraph.addEdge(0, 2, 1)
        # self.testGraph.addEdge(2, 3, 5) Cut the graph
        self.testGraph.addEdge(3, 4, 5)
        self.testGraph.addEdge(3, 5, 7)
        self.testGraph.addEdge(4, 5, 3)

    def testHotLink(self):
        hotEdges = self.testGraph.findHotEdge()
        self.assertNotIn((2, 3), hotEdges)
