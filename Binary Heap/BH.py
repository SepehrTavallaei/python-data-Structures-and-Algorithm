# A Binary Heap is a Binary Tree with following properties.
# - A Binary Heap is either Min Heap or Max Heap. In a Min Binary Heap, the key at root 
#       must be minimum among all keys present in Binary Heap. The same property must be 
#       recursively true for all nodes in Binary Tree.
# - It's a complete tree (All levels are completely filled except possibly the last level and the 
# last level has all keys as left as possible). This property of Binary Heap makes them
#  suitable to be stored in an array.

# common operation's on Binary heap:
# - Creation of Binary Heap,
# - Peek top of Binary Heap
# - Extract Min / Extract Max
# - Traversal of Binary Heap
# - Size of Binary Heap
# - Insert value in Binary Heap
# - Delete the entire Binary heap

# creation of Heap Binary:

class Heap:
    def __init__(self,size):
        self.customList = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size+1
def peekofHeap(rootNode): # O(1) time and space complexity
    if not rootNode:
        return
    return rootNode.customList[1]

def sizeofHeap(rootnode): # O(1) time and space complexity
    if not rootnode:
        return
    else:
        return rootnode.heapSize
def levelOrderTraversal(rootNode): # O(n) time complexity and O(1) space complexity
    if not rootNode:
        return
    else:
        for i in range(1,rootNode.heapSize+1): # O(n) time complexity
            print(rootNode.customList[i])

def heapifyTreeInsert(rootNode,index,heapType): # O(log n ) time and space complexity
    parentIndex = int(index/2)
    if index <=1:
        return
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
            heapifyTreeInsert(rootNode,parentIndex,heapType) # -----> O(log n) time complexity
    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
            heapifyTreeInsert(rootNode,parentIndex,heapType) # -----> O(log n) time complexity

def insertNode(rootNode, nodevalue,heapType): # O(log n) time complexity and space complexity
    if rootNode.heapSize +1 == rootNode.maxSize:
        return "the Binary Heap is full"
    rootNode.customList[rootNode.heapSize + 1] = nodevalue
    rootNode.heapSize +=1
    heapifyTreeInsert(rootNode,rootNode.heapSize,heapType)

def heapifyTreeExtract(rootNode,index,heapType):
    leftindex = 2* index
    rightindex = 2*index+1
    swapChild = 0 
    if rootNode.heapSize < leftindex:
        return
    elif  rootNode.heapSize == leftindex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftindex]:
                 temp = rootNode.customList[index]
                 rootNode.customList[index] = rootNode.customList[leftindex]
                 rootNode.customList[leftindex] = temp
            return
        else:
            if rootNode.customList[index] <  rootNode.customList[leftindex]:
                 temp = rootNode.customList[index]
                 rootNode.customList[index] = rootNode.customList[leftindex]
                 rootNode.customList[leftindex] = temp
            return 
    
    else:
        if heapType == "Min":
            if rootNode.customList[leftindex] < rootNode.customList[rightindex]:
                 swapChild = leftindex
            else: 
                swapChild = rightindex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        else:
            if rootNode.customList[leftindex] > rootNode.customList[rightindex]:
                 swapChild = leftindex
            else: 
                swapChild = rightindex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        heapifyTreeExtract(rootNode, swapChild,heapType)

def extractNode(rootNode,heaptype): # ===> O(log n) time and space complexity
    if rootNode.heapSize ==0 :
        return
    else:
        extractNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyTreeExtract(rootNode,1,heaptype)
        return extractNode

def deletBH(rootNode): # time and space complexity is O(1)
    if not rootNode:
        return
    else:
        rootNode.customList = None
    
            





newBinaryHeap = Heap(5)
insertNode(newBinaryHeap,4,"Max")
insertNode(newBinaryHeap,5,"Max")
insertNode(newBinaryHeap,2,"Max")
insertNode(newBinaryHeap,1,"Max")
extractNode(newBinaryHeap,"Max")
levelOrderTraversal(newBinaryHeap)