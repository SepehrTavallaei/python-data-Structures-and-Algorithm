class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class CSLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        node = self.head
        while node :
            yield node 
            if node.next == self.head:
                break
            node = node.next
    

    def creation_of_CSLL(self,value):
        newNode = Node(value)
        self.head = newNode
        newNode.next = newNode
        self.tail = newNode
        self.length+=1
    
    def insertCSLL(self,location,value):
        if self.head is None:
            return "the head refrenced is none you need to creat a csll at first"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
                self.length +=1
            elif location == 1:
                self.tail.next = newNode
                newNode.next = self.head
                self.tail = newNode
                self.length +=1
            else:
                index = 0
                tempNode = self.head
                while index < location-1:
                    tempNode = tempNode.next
                    index +=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                self.length +=1
            return "the node has been inserted successfully"


myCSLL = CSLL()
myCSLL.creation_of_CSLL(1)
myCSLL.insertCSLL(0,2)
myCSLL.insertCSLL(0,3)
myCSLL.insertCSLL(1,2)
print([node.value for node in myCSLL])
