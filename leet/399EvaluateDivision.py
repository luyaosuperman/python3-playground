import unittest
class Solution(unittest.TestCase):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        assert(len(equations) == len(values))
        #Directional graph, edge weight is the value

        self.nodes = {}
        self.edges = {}
        for i in range(len(equations)):
            equation = equations[i]
            value = values[i]
            node = equation[0]
            if node not in self.nodes:
                self.nodes[node]=[equation[1]]
            else:
                self.nodes[node].append(equation[1])

            node = equation[1]
            if node not in self.nodes:
                self.nodes[node]=[]

            node = equation[1]
            if node not in self.nodes:
                self.nodes[node]=[equation[0]]
            else:
                self.nodes[node].append(equation[0])

            node = equation[0]
            if node not in self.nodes:
                self.nodes[node]=[]

            assert(tuple(equation) not in self.edges)
            self.edges[tuple(equation)] = value

            #reverse edge
            euqation_reversed = list(reversed(equation))
            assert(tuple(euqation_reversed) not in self.edges)
            self.edges[tuple(euqation_reversed)] = 1.0 / value            

        #print(self.nodes)
        #print(self.edges)

        results = []
        for query in queries:
            if query[0] not in self.nodes or query[1] not in self.nodes:
                results.append(-1.0)
                continue

            if query[0] == query[1]:
                results.append(1.0)
                continue

            source = query[0]
            self.sink = query[1]

            self.visited = dict()
            self.reached = False
            for node in self.nodes:
                self.visited[node] = False

            #print()
            #print("query", query)
            result = self.DFS(source)
            if self.visited[self.sink] == True:
                #print("Found!")
                results.append(result)
            else:
                #print("No result")
                results.append(-1.0)

        #print(results)
        return results



    def DFS(self, node):
        #print("visiting", node)

        self.visited[node] = True
        result = -1
        for neighbor in self.nodes[node]:
            if neighbor == self.sink:
                #print("reached sink", neighbor)
                self.visited[self.sink] = True
                result = self.edges[(node, self.sink)]
                self.reached = True
                break
            if not self.reached and self.visited[neighbor] == False:
                #print("checking neighbor", neighbor)
                node_result = self.DFS(neighbor)
                if node_result != -1:
                    result = node_result * self.edges[(node,neighbor)]

        #print("node", node, "result", result)
        return result







    def test_1(self):
        equations = [ ["a", "b"], ["b", "c"] ]
        values = [2.0, 3.0]
        queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ] 
        expectes = [ 6.0, 0.5, -1.0, 1.0, -1.0 ]
        outputs = self.calcEquation(equations,values,queries)
        self.assertEqual(len(expectes),len(outputs))

        for i in range(len(expectes)):
            self.assertEqual(expectes[i], outputs[i])  

    def test_2(self):
        equations = [["a","b"],["b","c"],["bc","cd"]]
        values = [1.5,2.5,5.0]
        queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
        expectes = [3.75000,0.40000,5.00000,0.20000]
        outputs = self.calcEquation(equations,values,queries)
        self.assertEqual(len(expectes),len(outputs))

        for i in range(len(expectes)):
            self.assertEqual(expectes[i], outputs[i])  


    def test_3(self):
        equations = [["a","b"],["a","c"],["a","d"],["a","e"],["a","f"],["a","g"],["a","h"],["a","i"],["a","j"],["a","k"],["a","l"],["a","aa"],["a","aaa"],["a","aaaa"],["a","aaaaa"],["a","bb"],["a","bbb"],["a","ff"]]
        values = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,1.0,1.0,1.0,1.0,1.0,3.0,5.0]
        queries = [["d","f"],["e","g"],["e","k"],["h","a"],["aaa","k"],["aaa","i"],["aa","e"],["aaa","aa"],["aaa","ff"],["bbb","bb"],["bb","h"],["bb","i"],["bb","k"],["aaa","k"],["k","l"],["x","k"],["l","ll"]]
        expectes = [1.66667,1.50000,2.50000,0.14286,10.00000,8.00000,4.00000,1.00000,5.00000,0.33333,7.00000,8.00000,10.00000,10.00000,1.10000,-1.00000,-1.00000]
        outputs = self.calcEquation(equations,values,queries)
        self.assertEqual(len(expectes),len(outputs))

        for i in range(len(expectes)):
            try:
                self.assertAlmostEqual(expectes[i], outputs[i],4) 
            except:
                #print("failed query:", queries[i], "expected:", expectes[i], "output:", outputs[i])
                raise

if __name__ == '__main__':
    unittest.main()