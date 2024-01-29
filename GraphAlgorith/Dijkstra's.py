import heapq
class Edge:
    def __init__(self,weight,start_vertex,target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

class Node:
    def __init__(self,name):
        self.name = name
        self.visited = False
        # previous node that we come to this node
        self.predecessor = None
        self.neighbors = []
        self.min_distance = float("inf")
    
    def __lt__(self,other_node):
        return self.min_distance < other_node.min_distance
    def addEdge(self,weight,destination_vertex):
        edge = Edge(weight,self,destination_vertex)
        self.neighbors.append(edge)

# Dijkstra Algorithm

class Dijkstra:
    def __init__(self):
        self.heap = []
    
    def calculate(self,start_vertex):
        start_vertex.min_distance = 0
        heapq.heappush(self.heap,start_vertex)  
        while self.heap:
            #pop element with the lowest distance
            actuall_vertex = heapq.heappop(self.heap)
            if actuall_vertex.visited:
                continue
            # consider neighbors
            for edge in start_vertex.neighbors:
                start = edge.start_vertex
                target = edge.target_vertex
                new_distance = start.min_distance + edge.weight
                if new_distance < target.min_distance:
                    target.min_distance = new_distance
                    target.predecessor = start
                    # update the heap:
                    heapq.heappush(self.heap,target)
            actuall_vertex.visited = True
    
    def get_shortest_path(self,vertex):
        print(f"the shortest path to the vertex is: {vertex.min_distance}")
        actuall_vertex = vertex
        while actuall_vertex is not None:
            print(actuall_vertex.name,end=" ")
            actuall_vertex = actuall_vertex.predecessor
    


