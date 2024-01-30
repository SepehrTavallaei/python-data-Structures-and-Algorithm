class Edge:
    def __init__(self,vertex1,vertex2,weight):
        self.starting_vertex = vertex1
        self.target = vertex2
        self.weight = weight

class Node:
    def __init__(self,name):
        self.name = name
        self.neighbors = []
        self.parent = None
        self.min_distance = float("inf")
    
    def addEdge(self,vertex,weight):
        edge = Edge(self,vertex,weight)
        self.neighbors.append(edge)

def bellmanFordAlgorithm(vertices,Edges,starting_vertex): # Space complexity is O(v) and time complexity is O(VE)
    starting_vertex.min_distance = 0
    for i in range(0,len(vertices)-1): # O(V) time complexity
        for edge in Edges: # O(E) time complexity
            newDistance = edge[0].min_distance + edge[2]
            if newDistance < edge[1].min_distance:
                edge[1].min_distance = newDistance
                edge[1].parent = edge[0]
    for vertex in vertices: # O(E) time complexity
        if vertex != starting_vertex:
            print(vertex.name, vertex.min_distance)
        

nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeA.addEdge(nodeC,6)
nodeA.addEdge(nodeD,6)
nodeB.addEdge(nodeA,3)
nodeD.addEdge(nodeB,1)
nodeD.addEdge(nodeC,2)
nodeC.addEdge(nodeD,1)
nodeE.addEdge(nodeB,4)
nodeE.addEdge(nodeD,2)

vertices = [nodeA,nodeB,nodeC,nodeD,nodeE]
edges = [[nodeA,nodeC,6],[nodeA,nodeD,6],[nodeB,nodeA,3],[nodeD,nodeB,1],[nodeD,nodeC,2],[nodeC,nodeD,1],[nodeE,nodeB,4],[nodeE,nodeD,2]]

bellmanFordAlgorithm(vertices,edges,nodeE)
