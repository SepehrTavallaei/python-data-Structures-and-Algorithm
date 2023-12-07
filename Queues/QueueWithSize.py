class Queue():
    def __init__(self,MaxSize): # ---> O(n) Space Complexity because we are creating a list and O(1) time complexity
        self.items = MaxSize * [None]
        self.MaxSize = MaxSize
        self.start = -1
        self.top = -1
    
    def __str__(self):
        values = [str(item) for item in self.items]
        return ' '.join(values)
    
    def isFull(self): # --> space and time complexities of operations below are O(1)
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.MaxSize:
            return True
        else:
            return False
    
    def isEmpty(self):
        if self.top == -1:
            return True
        else : 
            return False
    
    def enqueue(self, value):
        if self.isFull():
            return "the queue is Full"
        else:
            self.top += 1
            if self.start == -1:
                self.start = 0
            self.items[self.top] = value
            return "the element is inserted at the end of Queue"
    def dequeue(self): # ---> space and time complexity both are O(1)
        if self.isEmpty():
            return "the Queue is empty"
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.MaxSize:
                self.start = 0
            else:
                self.start +=1
            self.items[start] = None
            return firstElement
    def peek(self):
        if self.isEmpty():
            return "the Queue is empty"
        else:
            return self.items[self.start]
    
    def delete(self):
        self.items = self.MaxSize * [None] # O(1) space complexity because additional space is not required and O(1) time complexity because all we are doing is updating some variables and not using any special loop 
        self.start = -1
        self.top = -1
    
    
customQueue = Queue(3)
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.isFull()) # returns True
print(customQueue) # 1 2 3
print(customQueue.enqueue(4)) # the queue is Full
print(customQueue) # again 1 2 3
print(customQueue.dequeue()) # 1 and the first index of list will be None
print(customQueue.dequeue()) # 2 and the first index of list will be None
print(customQueue) # None None 3
print(customQueue.peek()) # 3
