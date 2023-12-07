class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)
        
    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False
    def push(self, value):
        self.list.append(value)
        return "the element has been successfully inserted;"
    def pop(self):
        if self.is_empty():
            return "there is not any element in the stack"
        else:
            return self.list.pop()
    def peek(self):
        if self.is_empty():
            return "there is not any element on the Stack"
        else:
            return self.list[len(self.list)-1]
    def delete(self):
        self.list = None
        
customStack = Stack()
print(customStack.is_empty())
print(customStack.push(1))
print(customStack.push(2))
print(customStack.push(3))
print(customStack.is_empty())
customStack.pop()
print(customStack)
print(customStack.peek())