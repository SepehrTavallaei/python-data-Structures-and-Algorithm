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
                self.tail = newNode
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
    def traversalCSLL(self):
        if self.head == None:
            return "there is no element in the list"
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode= tempNode.next
                if tempNode == self.tail.next:
                    break
    def finder(self,value):
        if self.head is None:
            return "the list is empty"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == value:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "the node doesn't exist in this CSLL"
    def delete(self,location):
        if self.head is None :
            return "the list is empty"
        if location == 0:
            if self.tail == self.head:
                self.head.next = None
                self.head = None
                self.tail = None
            else: 
                self.head = self.head.next
                self.tail.next = self.head
        elif location == 1:
            if self.tail == self.head:
                self.head.next = None
                self.head = None
                self.tail = None
            else:
                tempNode = self.head
                while tempNode is not None:
                    if tempNode.next == self.tail:
                        break
                    tempNode = tempNode.next
                tempNode.next = self.head
                self.tail = tempNode
        else:
            tempNode = self.head
            index = 0 
            while index < location-1:
                tempNode = tempNode.next
                index +=1
            nextNode = tempNode.next
            tempNode.next = nextNode.next
    def deleteAll(self):
        self.head = None
        self.tail.next = None
        self.tail = None



circularSLL = CircularLinkedList()
print(circularSLL.creatCSLL(1))
circularSLL.insertCSLL(0,0)
circularSLL.insertCSLL(2,1)
circularSLL.insertCSLL(3,1)
circularSLL.insertCSLL(2,2)

circularSLL.traversalCSLL()
print(circularSLL)
circularSLL.delete(0)
circularSLL.delete(1)
print(circularSLL)
circularSLL.deleteAll()
print(circularSLL)