import heapq

class Edge:
    def __init__(self,start_vertex,destination_vertex,weight):
        self.start_vertex = start_vertex
        self.destination_vertex = destination_vertex
        self.weight = weight

class Node:
    def __init__(self,name):
        self.name = name
        self.neighbors = []
        self.min_distance = float("inf")
        self.predecessor = None
        self.visited = False
    
    def addEdge(self,vertex,weight):
        edge = Edge(self,vertex,weight)
        self.neighbors.append(edge)
    
    def __lt__(self,vertex):
        return self.min_distance < vertex.min_distance

class Dijkstra:
    def __init__(self):
        self.heap = []

    def calculate(self,starting_vertex):
        starting_vertex.min_distance = 0
        heapq.heappush(self.heap,starting_vertex)
        while self.heap:
            # pop element with the lowest distance
            actual_vertex = heapq.heappop(self.heap)
            if actual_vertex.visited:
                continue
            for edge in actual_vertex.neighbors:
                start_vertex = edge.start_vertex
                target_vertex = edge.destination_vertex
                new_distance = edge.weight + start_vertex.min_distance
                if new_distance < target_vertex.min_distance:
                    target_vertex.min_distance = new_distance
                    target_vertex.predecessor = start_vertex
                    # update the heap
                    heapq.heappush(self.heap,target_vertex)
            actual_vertex.visited = True

    def getShortestPath(self,vertex):
        print(f"the shortest path to the vertex is: {vertex.min_distance}")
        actuall_vertex = vertex
        while actuall_vertex is not None:
            print(actuall_vertex.name,end=" ")
            actuall_vertex = actuall_vertex.predecessor

nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")
nodeH = Node("H")

nodeA.addEdge(nodeB,6)
nodeA.addEdge(nodeC,10)
nodeA.addEdge(nodeD,9)
nodeB.addEdge(nodeE,16)
nodeB.addEdge(nodeF,13)
nodeB.addEdge(nodeD,5)
nodeD.addEdge(nodeF,8)
nodeD.addEdge(nodeH,7)
nodeC.addEdge(nodeD,6)
nodeC.addEdge(nodeH,5)
nodeC.addEdge(nodeG,21)
nodeH.addEdge(nodeF,2)
nodeH.addEdge(nodeG,14)
nodeE.addEdge(nodeG,10)
nodeF.addEdge(nodeE,4)
nodeF.addEdge(nodeG,12)

algorith = Dijkstra()

algorith.calculate(nodeA)
algorith.getShortestPath(nodeG)