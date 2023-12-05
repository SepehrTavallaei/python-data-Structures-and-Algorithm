class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class CDLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def CreationOfDLL(self,value):
        firstNode = Node(value)
        firstNode.next = firstNode
        firstNode.prev = firstNode
        self.head = firstNode
        self.tail = firstNode
    def __str__(self):
        if self.head is None:
            return " "
        else: 
            temp_node = self.tail.next
            result = ''
            while temp_node:
                result += str(temp_node.value)
                temp_node = temp_node.next
                if temp_node == self.tail.next: 
                    break
                result += ' -> '
            return result
    def insert(self , value, location):
        if self.head is None and location == 0:
            self.CreationOfDLL(value)
        elif location == 0:
            newNode = Node(value)
            self.tail.next = newNode
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            newNode.prev = self.tail
        elif location == 1:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode
            newNode.next = self.head
        else:
            newNode = Node(value)
            temp_node = self.head
            cur = 0
            while cur < location-1:
                cur+=1
                temp_node = temp_node.next
            nextNode = temp_node.next
            temp_node.next = newNode
            nextNode.prev = newNode
            newNode.prev = temp_node
            newNode.next = nextNode

        

cdll  = CDLL()
cdll.CreationOfDLL(2)
cdll.insert(4,0)
cdll.insert(3,1)
cdll.insert(5,0)
cdll.insert(7,2)
print(cdll)