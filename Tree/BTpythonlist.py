class BinaryTree:
    def __init__(self,size):
        self.customlist = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size
    
    def insertNode(self,value):
        if self.lastUsedIndex+1 == self.maxSize:
            return "the binary tree is full"
        if not value in self.customlist:
            self.customlist[self.lastUsedIndex+1] = value
            self.lastUsedIndex +=1
            return "the value has been successfully inserted"
        return "the value is already in the tree"
    def searchNode(self,nodevalue): # time complexity O(n) space complexity : O(1)
        if nodevalue in self.customlist:
            return "success"
        return "not found"
    
    def preorderTraversal(self,index): # ===> O(N) space comlpexity
        if index > self.lastUsedIndex:
            return None
        print(self.customlist[index])
        self.preorderTraversal(index*2) #====> o(n/2) time complexity
        self.preorderTraversal(index*2+1)# ===> O(n/2) time complexity
    
    def inorderTraversal(self,index):
        if index>self.lastUsedIndex:
            return None
        else:
            self.inorderTraversal(index*2)
            print(self.customlist[index])
            self.inorderTraversal(index*2+1)

    def postOrderTraversal(self,index):
        if index>self.lastUsedIndex:
            return None
        else:
            self.inorderTraversal(index*2)
            self.inorderTraversal(index*2+1)
            print(self.customlist[index])
    def levelOrderTraversal(self):
        for i in self.customlist:
            if i != None:
                print(i)
    def deleteNode(self,value):
        if self.lastUsedIndex == 0:
            return "the Binary Tree is empty"
        for i in range(len(self.customlist)):
            if self.customlist[i] == value:
                self.customlist[i] = self.customlist[self.lastUsedIndex]
                self.customlist[self.lastUsedIndex] = None
                self.lastUsedIndex-=1
                return "the node has been successfully deleted"
    
    def deleteEntireList(self):
        self.customlist = self.maxSize * [None]
        self.lastUsedIndex = 0

    
    

newBT = BinaryTree(8) # ----> spacecomplexity : O(n) / time complexity is: O(1)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold") 
newBT.insertNode("tea")
newBT.insertNode("coffee")
# newBT.preorderTraversal(1)
# newBT.inorderTraversal(1)
newBT.levelOrderTraversal()