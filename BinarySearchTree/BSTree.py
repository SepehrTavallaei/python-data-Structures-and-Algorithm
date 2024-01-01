# BinarySearch Tree is a Binary Tree which it has some extra properties:
# - In the left subtree the value of a node is less than or equal to its parent node's value.
# - In the right subtree the value of a node is greater than its parent node's value
# Why do we need binary search tree?
# - It performs faster than Binary Tree when inserting and deleting nodes

from QueueLinkedList import Queue

class BinarySearchTree:
    def __init__(self,data):
        self.data = data
        self.rightChild = None
        self.leftChild = None

newBST = BinarySearchTree(None)

def insert(rootNode,Node): #----> O(n) time complexity and O(log n) space complexity
    if rootNode.data == None:
        rootNode.data = Node
    elif Node <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BinarySearchTree(Node) #---O(n/2) time complexity
        else:
            insert(rootNode.leftChild,Node)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BinarySearchTree(Node) #----O(n/2) time complexity
        else:
            insert(rootNode.rightChild,Node)


def PreOrderTraversal(rootNode): #O(n) time and space complexity
    if rootNode is None:
        return "the Binary search tree is empty"
    print(rootNode.data)
    PreOrderTraversal(rootNode.leftChild)
    PreOrderTraversal(rootNode.rightChild)
    return 

def inorderTraversal(rootNode):
    if rootNode is None:
        return 
    inorderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inorderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if rootNode is None:
        return 
    inorderTraversal(rootNode.leftChild)
    inorderTraversal(rootNode.rightChild)
    print(rootNode.data) 

def LevelOrderTraversal(rootNode): # ---> O(n) time and space complexity
    if rootNode is None:
        return None
    customQueue = Queue()
    customQueue.enqueue(rootNode)
    while not customQueue.isEmpty():
        root = customQueue.dequeue()
        print(root.value.data)
        if root.value.leftChild is not None:
            customQueue.enqueue(root.value.leftChild)
        if root.value.rightChild is not None:
            customQueue.enqueue(root.value.rightChild)

def search(rootNode,value): # O(log n ) time complexity 

    if rootNode.data == value:
        print("found")
    elif rootNode.data > value:
        if rootNode.leftChild:
            search(rootNode.leftChild,value)
        else:
            print("not found")
            return
    else:
        if rootNode.rightChild:
            search(rootNode.rightChild,value)
        else:
            print("not found")
            return 


def minValue(bsTree):
    current = bsTree
    while (current.leftChild is not None):
        current = current.leftChild
    return current

 
def delete(rootNode,Nodevalue):
    if rootNode is None:
        return None
    
    if Nodevalue < rootNode.data:
        rootNode.lefttChilf = delete(rootNode.leftChild, Nodevalue)
    elif Nodevalue>rootNode.data:
        rootNode.rightChild = delete(rootNode.rightChild,Nodevalue)
    
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode.leftChild = None
            return temp
        
        temp = minValue(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = delete(rootNode.rightChild, temp.data)
    return rootNode

def deleteEntireBinartSearchTree(rootNode):
    rootNode.data = None
    rootNode.rightChild = None
    rootNode.leftChild = None
    return " the binary search has been deleted successfully"

    

insert(newBST, 70)
insert(newBST,50)
insert(newBST,90)
insert(newBST, 30)
insert(newBST,60)
insert(newBST,80)
insert(newBST,100)
insert(newBST,20)
insert(newBST,40)
delete(newBST,100)
LevelOrderTraversal(newBST )
