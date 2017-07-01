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
        
        """record the edge and its weight
        
        every edge is recorded twice
        {
            node1: {
                node2: 1, 
                node3: 2
            },
            ...
            node3: {
                node1: 2
            }
        }
        """
        self.edges = dict() 

        """record the frequency of edge being used
        only record once per edge
        {
            (smallerNode, largerNode): count, 
            ...
        }
        """
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
        nodesDistance = [math.inf] * self.numberOfNodes
        nodesPrevious = [-1] * self.numberOfNodes

        nodesDistance[node] = 0
        nodesPrevious[node] = node

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
        return nodesPrevious, nodesDistance

    def findHotEdge(self):
        """
        find hot path based on dijkstra
        """
        for src in range(self.numberOfNodes):
            nodesPrevious, nodesDistance = self.dijkstra(src)
            for dest in range(self.numberOfNodes):
                #find all path from different nodes to source
                if dest != src and nodesPrevious[dest] != -1:
                    pre = nodesPrevious[dest]
                    while pre != dest:
                        self.logAnEdge(pre, dest)
                        dest = pre
                        pre = nodesPrevious[dest]
        xPrint(self.edgesUsed)
        return self.edgesUsed

    def logAnEdge(self, node1, node2):
        """
        log an edge to the "frequency list"
        """
        if node1 < node2:
            node = (node1, node2)
        else:
            node = (node2, node1)

        if node not in self.edgesUsed:
            self.edgesUsed[node] = 1
        else:
            self.edgesUsed[node] += 1



if __name__ == "__main__":
    graph = UndirectionalGraph(3)
    graph.addEdge(0,1,1)
    graph.addEdge(0,2,4)
    graph.addEdge(1,2,2)
    graph.dijkstra(0)
    graph.findHotEdge()


    print("******************")
    graph = UndirectionalGraph(6)
    graph.addEdge(0,1,2)
    graph.addEdge(1,2,3)
    graph.addEdge(0,2,1)
    graph.addEdge(2,3,5)
    graph.addEdge(3,4,5)
    graph.addEdge(3,5,7)
    graph.addEdge(4,5,3)
    graph.dijkstra(0)
    graph.findHotEdge()

    print("******************")
    graph = UndirectionalGraph(6)
    graph.addEdge(0,1,2)
    graph.addEdge(1,2,3)
    graph.addEdge(0,2,1)
    #graph.addEdge(2,3,5) Cut the graph
    graph.addEdge(3,4,5)
    graph.addEdge(3,5,7)
    graph.addEdge(4,5,3)
    graph.dijkstra(0)
    graph.findHotEdge()
