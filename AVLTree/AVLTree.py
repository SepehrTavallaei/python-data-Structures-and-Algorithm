# An AVL tree is a self-balancing Binary Search Tree (BST) where the difference between
# heights of left and right subtrees cannot be more than one for all nodes. 

# If at any time heights of left and right subtrees differ by more than one, then rebalancing is 
# done to restore AVL property,  this process is called rotation.

# for better and more explecit details please visit the PDF file that I wrote (the file name is: why do we need AVL tree)
import QueueLinkedList 
class AVLNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1 

def preorderTraversal(rootNode):
    if not rootNode:
        return None
    
    print(rootNode.data)
    preorderTraversal(rootNode.leftChild)
    preorderTraversal(rootNode.rightChild)


def inorderTraversal(rootNode):
    if not rootNode:
        return None
    
    preorderTraversal(rootNode.leftChild)
    print(rootNode.data)
    preorderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return None
    
    preorderTraversal(rootNode.leftChild)
    preorderTraversal(rootNode.rightChild)
    print(rootNode.data)


def levelOrderTraversal(rootNode):
    if rootNode is None:
        return rootNode
    else:
        customQueue = QueueLinkedList.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)


def searchNode(rootNode,value):
    if  rootNode is None:
        return 
    else:
        if rootNode.data == value:
            print("found")
        elif rootNode.data > value:
            searchNode(rootNode.leftChild,value)
        else:
            searchNode(rootNode.rightChild,value)

def get_height(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

def rightRotate(disbalanceNode):
      newRoot = disbalanceNode.leftChild
      disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild
      newRoot.rightChild = disbalanceNode
      disbalanceNode.height = 1 + max(get_height(disbalanceNode.leftChild),get_height(disbalanceNode.rightChild))

def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.rightChild
    disbalanceNode.rightChild = disbalanceNode.rightChild.leftChild
    newRoot.leftChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)
    
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotate(rootNode)
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotate(rootNode)
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode

def getMinValueNode(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValueNode(rootNode.leftChild)

def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        temp = getMinValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    balance = getBalance(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) >= 0:
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) <= 0:
        return leftRotate(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) < 0:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) > 0:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    
    return rootNode

def deleteAVL(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The AVL has been successfully deleted"
    

tree = AVLNode(70)
left = AVLNode(60)
right = AVLNode(80)
tree.leftChild = left
tree.rightChild = right
rightleft = AVLNode(75)
rightRight = AVLNode(90)
right.leftChild = rightleft
right.rightChild = rightRight
levelOrderTraversal(tree)

searchNode(tree,90)