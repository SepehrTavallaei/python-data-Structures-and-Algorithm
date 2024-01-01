class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue():
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        if self.head == None:
            return True
        return False
    
    def __str__(self):
        if self.isEmpty():
            return "the Queue is empty"
        else :
            tempNode = self.head
            result = ""
            while tempNode:
                result += str(tempNode.value) + " "
                tempNode = tempNode.next
            return result

    def enqueue(self,value): # ---> O(1) time and space complexity
        newElement = Node(value)
        if self.isEmpty():
            self.head = newElement
            self.tail = newElement
        else:
            lastElement = self.tail
            lastElement.next = newElement
            self.tail = newElement
    
    def dequeue(self):
        if self.isEmpty():
            return "the Queue is empty"
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
    
    def peek(self):
        if self.isEmpty():
            return "the Queue is empty"
        else:
            return self.head.value
    
    def delete(self):
        if self.isEmpty():
            return "the Queue is empty"
        else:
            self.head = None
            self.tail = None

customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
customQueue.dequeue()
print(customQueue) # 2 3