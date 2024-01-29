from collections import deque # imported to lessen the time complexity of BFS traversal of the Graph

class Graph:
    def __init__(self):
        self.gdict = {}
    
    def add_vertex(self,vertex):
        if vertex not in self.gdict.keys():
            self.gdict[vertex] = []
            return True
        return False
    
    def add_Edge(self,vertex1,vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            self.gdict[vertex1].append(vertex2)
            self.gdict[vertex2].append(vertex1)
            return True
        return False
    
    def removeEdge(self,vertex1,vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            self.gdict[vertex1].remove(vertex2)
            self.gdict[vertex2].remove(vertex1)
            return True
        return False
    
    def BFS(self,vertex): # O(V+E) time complexity O(V) space complexity
        visited = set()
        visited.add(vertex)
        queue = deque([vertex])
        while queue:
            current_vertex = queue.popleft()
            print(current_vertex)
            for node in self.gdict[current_vertex]:
                if node  not in visited:
                    visited.add(node)
                    queue.append(node)
    
    def DFS(self,vertex,visited):
        visited = set()
        stack = [vertex]
        while stack:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
                for adjacent_vertex in self.gdict[current_vertex]:
                    if adjacent_vertex not in visited:
                        stack.append(adjacent_vertex)
                        
        


graph = Graph()

graph.add_vertex("a")
graph.add_vertex("b")
graph.add_vertex("c")
graph.add_vertex("d")
graph.add_vertex("e")
graph.add_Edge("a","b")
graph.add_Edge("a","c")
graph.add_Edge("b","e")
graph.add_Edge("c","d")
graph.add_Edge("d","e")

graph.BFS("a")