from collections import defaultdict

class Graph:
    def __init__(self,numberVerices):
        self.graph = defaultdict(list)
        self.numbervertices = numberVerices
    
    def addEdge(self,vertex,edge):
        self.graph[vertex].append(edge)
    
    def topologicalSortUtil(self,v,visited,stack):
        visited.append(v)
        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortUtil(i,visited,stack)
        stack.insert(0,v)

    def TopologicalSort(self): # O(E+V) time complexity & space complexity is o(E+V)
        visited = []
        stack = []

        for k in list(self.graph): # O(E+V) time complexity
            if k not in visited:
                self.topologicalSortUtil(k,visited,stack) # O(E) time complexity
        print(stack)


customGraph = Graph(8)

customGraph.addEdge ("A","C")
customGraph.addEdge("C","E")
customGraph.addEdge("E","H")
customGraph.addEdge("E","F")
customGraph.addEdge("F","G")
customGraph.addEdge ("B","D")
customGraph.addEdge ("B","C")
customGraph.addEdge("D","F")

customGraph.TopologicalSort()