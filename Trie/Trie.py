class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insertString(self,word): # O(n) time complexity and the space complexity in the worst case (no match found in the Trie) O(n) note: n is the lengh of the given string
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})
                current = node
        current.endOfString = True
        print("successfully inserted")
    def search(self,word):
        current = self.root
        for i in word:
            if not current.children.get(i):
                return False
        return True
    

def deleteString(root,word,index):
    ch = word[index]
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted = False

    if len(currentNode.children) > 1:
        deleteString(currentNode,word,index)
        return False
    if index == len(word)-1:
        if len(currentNode.children) >-1:
            currentNode.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True
    if currentNode.endOfString == True:
        deleteString(currentNode,word,index+1)
        return False
    canThisNodeBeDeleted = deleteString(currentNode,word,index+1)
    if canThisNodeBeDeleted:
        root.children.pop(ch)
        return True
    else:
        return False
        

newTrie = Trie()
newTrie.insertString("APP")
newTrie.insertString("APPL")
newTrie.search("AP")