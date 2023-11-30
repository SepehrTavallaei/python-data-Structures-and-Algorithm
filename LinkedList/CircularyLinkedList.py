# the same as singly linked list but the diffrence is that the last node ( the node before tail) points to the first node

class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.lenght = 0
    
    def __iter__(self):
        node = self.head
        while node :
            yield node 
            if node.next == self.head:
                break
            node = node.next
    def creatCSLL(self,nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        self.lenght +=1
        return "the CSLL has been created"

    def insertCSLL(self,value,location):
        if self.head is None:
            return "the head refrence is none"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location ==1:
                newNode.next = self.tail.next
                self.tail.next = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index+=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return "the node has been successfuly inserted"

circularSLL = CircularLinkedList()
print(circularSLL.creatCSLL(1))
circularSLL.insertCSLL(0,0)
circularSLL.insertCSLL(2,1)
circularSLL.insertCSLL(3,1)
circularSLL.insertCSLL(2,2)
print([node.value for node in circularSLL])

 