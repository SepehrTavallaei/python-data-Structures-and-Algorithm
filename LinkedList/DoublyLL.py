class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
    def creationDLL(self , value):
        newNode = Node(value)
        newNode.next = None
        newNode.prev = None
        self.head = newNode
        self.tail = newNode
        return "the list has been created successfully!"
    def __str__(self):
        if self.head == None:
            return "the list is empty"
        else:
            tempNode = self.head
            result = ""
            while tempNode:
                result += str(tempNode.value)
                if tempNode.next:
                    result+=" <=> "
                tempNode=tempNode.next
            return result
    def insertDLL(self,value,location):
        if location==0 and self.head==None:
            return self.creationDLL(value)
        elif location == 0:
            newNode = Node(value)
            secondNode = self.head
            secondNode.prev = newNode
            newNode.next = secondNode
            self.head = newNode
        elif location == 1:
            newNode = Node(value)
            tempNode = self.head
            while tempNode is not self.tail:
                tempNode = tempNode.next
            newNode.prev = tempNode
            tempNode.next = newNode
            self.tail = newNode
        else:
            newNode = Node(value)
            tempNode = self.head
            index = 0
            while index < location :
                tempNode = tempNode.next
                index+=1
            nextNode = tempNode.next
            nextNode.prev = newNode
            tempNode.next = newNode
            newNode.next = nextNode
            newNode.prev = tempNode
    def deletItem(self,location):
        if ((location==0 or location==1) and (self.tail == self.head)):
            self.head = None
            self.tail = None
        elif location ==0:
            firstNode = self.head.next
            self.head = firstNode
            firstNode.prev = None
        elif location ==1:
            tempNode = self.head
            while tempNode.next is not self.tail:
                tempNode = tempNode.next
            tempNode.next = None
            self.tail = tempNode
        else:
            tempNode = self.head
            index = 0
            while index < location:
                index +=1
                tempNode = tempNode.next
            deletedNode = tempNode.next
            tempNode.next = deletedNode.next
            deletedNode.prev = tempNode
    def delALL(self):
        tempNode = self.head
        while tempNode:
            tempNode.prev = None
            tempNode = tempNode.next
        self.head = None
        self.tail = None

    
doublyLinkedList = DLL()
doublyLinkedList.creationDLL(1)
doublyLinkedList.insertDLL(2,1)
doublyLinkedList.insertDLL(3,1)
doublyLinkedList.insertDLL(0,0)
doublyLinkedList.insertDLL(22,2)
print(doublyLinkedList)
doublyLinkedList.deletItem(0)
print(doublyLinkedList)
doublyLinkedList.delALL()
print(doublyLinkedList)

                