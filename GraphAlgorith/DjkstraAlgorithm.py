import heapq
class Edge:
    def __init__(self,vertex1,vertex2,weight):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weigth = weight

class Node:
    def __init__(self,name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.neighbors = []
        self.min_distance = float("inf")
    
    def __lt__(self,other_node):
        return self.min_distance < other_node.min_distance
    
    def add_Edge(self,vertex2,weight):
        edge = Edge(self,vertex2,weight)
        self.neighbors.append(edge)

class Dijkstra:
    def __init__(self):
        self.heap = []
    
    def calculate(self,starting_vertex):
        starting_vertex.mindistance = 0
        self.heap.append(starting_vertex)
        while self.heap:
            selected_vertex = heapq.heappop(self.heap) 
            if selected_vertex.visited:
                continue
            