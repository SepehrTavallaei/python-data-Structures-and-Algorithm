import heapq
class Edge:
    def __init__(self,vertex1,vertex2,weight):
        self.starting_vertex = vertex1
        self.destination_vertex = vertex2
        self.weight = weight
class Node:
    def __init__(self,name):
        self.name = name
        self.neighbors = []
    
    def Add_Edge(self,vertex2,weight):
        if vertex2 is Node and weight is int:
            destination_vertex = Edge(self,vertex2,weight)
            self.neighbors.append(destination_vertex)