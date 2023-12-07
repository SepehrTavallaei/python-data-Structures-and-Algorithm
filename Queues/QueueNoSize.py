class Queue:
    def __init__(self):
        self.items = []
    
    def __str__(self): #---> O(N) time complexity and O(n) space complexity
        values = [str(item) for item in self.items]
        return ' '.join(values)
    def is_empty(self): # -----> O(1) time and space complexity
        if self.items == []:
            return True
        else:
            return False
    def enqueue(self,value):
        self.items.append(value) # in the worst case O(n^2) time complexity because we have to go trough at the end of the list and O(1) space complexity
        return "the element is inserted at the end of queue"

    def dequeue(self): # ---> O(n) time complexity
        if self.is_empty(): # ---> O(1) space and time complexity
            return "there is not any element in the queue"
        else:
            return self.items.pop(0) #----> O(n) time complexity and O(1) space complexity
    
    def peek(self): # ---> O(1) time complexity and space complexity
        if self.is_empty():
            return "there is not any element in the queue"
        else:
            return self.items[0]

    def delete(self): # ---> space and time complexity os O(1 )
        self.items = None

customQuue = Queue()
print(customQuue.is_empty())
customQuue.enqueue(1)
customQuue.enqueue(2)
customQuue.enqueue(3)
print(customQuue)
print(customQuue.dequeue())
print(customQuue)
    
        