class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class MultiStack:
    def __init__(self,stackSize):
        self.numberstacks = 3
        self.customList = [0] * (stackSize* self.numberstacks)
        self.sizes = [0] * self.numberstacks
        self.stackSize = stackSize
    
    def isfull(self,stacknum):
        if self.sizes[stacknum] == self.stackSize:
            return True
        else :
            return False
    
    def isempty(self,stacknum):
        if self.sizes[stacknum] == 0:
            return True
        else : 
            return False
    
    def indexOfTop(self,stacknum):
        offset = stacknum * self.stackSize
        return offset + self.sizes[stacknum] -1 

