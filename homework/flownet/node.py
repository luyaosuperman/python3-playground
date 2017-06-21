class Node():
    """
    A node in the graph
    """

    def __init__(self, nodeId):
        """
        Init the node
        """
        self.nodeId = nodeId
        self.adjacentNodes = [] # Adjacency list
        self.adjacentWeights = [] # weight of the edge

    def addNeighbor(self, node, weight)
        """
        add a node, and the weight of corresponding edge, to the list
        """
        self.adjacentNodes.append(node)
        self.adjacentWeights.append(weight)

        if len(self.adjacentNodes) != len(self.adjacentWeights):
            raise ValueError("something wrong within the node")

        