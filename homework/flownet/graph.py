import heapq
import math
from xprint import xPrint, printStack

class UndirectionalGraph():
    """
    Graph itself composed of nodes and edges
    """

    def __init__(self, numberOfNodes):
        """
        Init the graph
        """
        # assume nodes start from 0, stop at numberOfNodes - 1
        self.numberOfNodes = numberOfNodes 
        
        # record the edge and its weight
        # every edge is recorded twice
        # {node1: {node2:1, node3:2}, ...}
        self.edges = dict() 

        # record the frequency of edge being used
        # only record once per edge
        # {(smallerNode, largerNode):count, ...}
        self.edgesUsed = dict() 

    def addEdge(self, node1, node2, weight):
        """
        add edges to the graph
        """
        if node1 not in self.edges:
            self.edges[node1] = dict()

        if node2 not in self.edges:
            self.edges[node2] = dict()

        self.edges[node1][node2] = weight
        self.edges[node2][node1] = weight
        xPrint(self.edges)


    def dijkstra(self, node):
        """
        Calculate the shortest spannning tree from a node
        """
        #nodesVisisted = [False] * self.numberOfNodes
        nodesDistance = [math.inf] * self.numberOfNodes
        nodesPrevious = [-1] * self.numberOfNodes

        nodesDistance[node] = 0

        minpq = []
        for node in range(self.numberOfNodes):
            heapq.heappush(minpq, [nodesDistance[node],node]) # value of minpq, item

        while len(minpq) > 0:
            item = heapq.heappop(minpq)
            [currentDist, currentNode] = item
            for neighborNode in self.edges[currentNode]:
                distanceToNeighborNode = self.edges[currentNode][neighborNode]
                distance = nodesDistance[currentNode] + distanceToNeighborNode
                if distance < nodesDistance[neighborNode]:
                    nodesDistance[neighborNode] = distance
                    nodesPrevious[neighborNode] = currentNode
                    # decrease priority of the item
                    item[0] = distance
                    heapq.heapify(minpq)
        xPrint(nodesDistance)
        xPrint(nodesPrevious)

if __name__ == "__main__":
    graph = UndirectionalGraph(3)
    graph.addEdge(0,1,1)
    graph.addEdge(0,2,4)
    graph.addEdge(1,2,2)
    graph.dijkstra(0)


    graph = UndirectionalGraph(6)
    graph.addEdge(0,1,2)
    graph.addEdge(1,2,3)
    graph.addEdge(0,2,1)
    graph.addEdge(2,3,5)
    graph.addEdge(3,4,5)
    graph.addEdge(3,5,7)
    graph.addEdge(4,5,3)
    graph.dijkstra(0)





        






