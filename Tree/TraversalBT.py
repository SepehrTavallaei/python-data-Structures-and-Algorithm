# 1)BREADTH FIRST SEACRH (BFS):
#       it has only one way of traversal and that is called level order traversal
# 2)DEAPTH FIRST SEARCH:
#       there are three ways to do DFS:
#           1) - Preorder traversal
#           2) Inorder traversal
#           3) Post order traversal

import QueueLinkedList


class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.RightChild = None

tree = BinaryTree("drink")
cold = BinaryTree("cold")
hot = BinaryTree("hot")
coffee = BinaryTree("coffee")
tea = BinaryTree("tea")
milk = BinaryTree("milk")
water = BinaryTree("water")
lattee = BinaryTree("Latte")
arabika = BinaryTree("Arabika")
tree.leftChild = hot
tree.RightChild = cold
cold.leftChild = milk
cold.RightChild = water
hot.leftChild = coffee
hot.RightChild = tea
coffee.leftChild = lattee
coffee.RightChild = arabika

     
def preorderTraversal(rootNode): # ----> O(n) time complexity
    if not rootNode:
        return None
    print(rootNode.data)
    preorderTraversal(rootNode.leftChild) # ---> O(n/2) time complexity
    preorderTraversal(rootNode.RightChild)# ----> o(n/2) time complexity



def inorderTraversal(rootNode): # ----> O(n) time complexity
    if not rootNode:
        return None
    inorderTraversal(rootNode.leftChild) # ---> O(n/2) time complexity
    print(rootNode.data)
    inorderTraversal(rootNode.RightChild)# ----> o(n/2) time complexitys



def postorderTraversal(rootNode): # ----> O(n) time complexity
    if not rootNode:
        return None
    postorderTraversal(rootNode.leftChild) # ---> O(n/2) time complexity
    postorderTraversal(rootNode.RightChild)# ----> o(n/2) time complexitys
    print(rootNode.data)



def levelorderTraversal(rootNode):# -----> O(n) time complexity and O(n) space complexity because we are creating a Queue and inserting n elements to it so this will take space in the memory
    if not rootNode:
        return None
    customqueue = QueueLinkedList.Queue()
    customqueue.enqueue(rootNode)
    while not(customqueue.isEmpty()):
        root = customqueue.dequeue()
        print(root.value.data)
        if root.value.leftChild is not None: 
            customqueue.enqueue(root.value.leftChild) 
        if root.value.RightChild is not None:
            customqueue.enqueue(root.value.RightChild)


def search(rootNode,node): # time and space complexity O(n)
    if not rootNode:
        return None
    else:
        customqueu = QueueLinkedList.Queue()
        customqueu.enqueue(rootNode)
        while not(customqueu.isEmpty()):
            root = customqueu.dequeue()
            if node == root.value.data:
                return "element found! "
            else: 
                if root.value.leftChild is not None:
                    customqueu.enqueue(root.value.leftChild)
                if root.value.RightChild is not None:
                    customqueu.enqueue(root.value.RightChild)

def insert(rootNode,Node): # time and space complexity is O(n)
    if not rootNode:
        rootNode = Node
    else:
        customQueue = QueueLinkedList.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.leftChild is None:
                root.value.leftChild = Node
                break
            else:
                customQueue.enqueue(root.value.leftChild)
            if root.value.RightChild is None:
                root.value.RightChild = Node
                break
            else: 
                customQueue.enqueue(root.value.RightChild)
def getDeepestNode(rootNode):
    if not rootNode:
        return None
    else:
        customqueue = QueueLinkedList.Queue()
        customqueue.enqueue(rootNode)
        while not customqueue.isEmpty():
            root = customqueue.dequeue()
            if root.value.leftChild is not None: 
                customqueue.enqueue(root.value.leftChild) 
            if root.value.RightChild is not None:
                customqueue.enqueue(root.value.RightChild)
            
        deepestNode = root.value
        return deepestNode

def DeleteDeepestNode(rootNode,dNode):
    customqueue = QueueLinkedList.Queue()
    customqueue.enqueue(rootNode)
    while not customqueue.isEmpty():
        root = customqueue.dequeue()
        if root.value is dNode:
            root.value = None
        if root.value.RightChild:
            if root.value.RightChild is dNode:
                root.value.RightChild = None
            else:
                customqueue.enqueue(root.value.RightChild)
            
        if root.value.leftChild:
            if root.value.leftChild is dNode:
                root.value.leftChild = None
            else:
                customqueue.enqueue(root.value.leftChild)

def deleteNode(rootNode, node):
    if not rootNode:
        return "the binary tree does not exist"
    else:
        customqueue = QueueLinkedList.Queue()
        customqueue.enqueue(rootNode)
        while not customqueue.isEmpty():
            root = customqueue.dequeue()
            if rootNode.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                DeleteDeepestNode(rootNode,dNode)
                return "the node has been successfully deleted"
            if root.value.leftChild is not None: 
                customqueue.enqueue(root.value.leftChild) 
            if root.value.RightChild is not None:
                customqueue.enqueue(root.value.RightChild)
        return "Failed to delete"

def deleteBT(rootNode): #-----> time complexity O(1) spacecomplexity : O(1)
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.RightChild = None
    return "the binary tree has been successfully deleted"




    




