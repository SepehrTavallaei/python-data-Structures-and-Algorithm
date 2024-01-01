class TreeNode:
    def __init__(self,data,children=[]):
        self.data = data
        self.children = children
    
    def __str__(self,level = 0):
        result = "  " * level + str(self.data) + "\n"
        for child in self.children:
            result += child.__str__(level + 1)
        return result
    
    def addChild(self,TreeNode):
        self.children.append(TreeNode)


Tree = TreeNode("even numbers",[])
two = TreeNode("2",[])
Tree.addChild(two)
four = TreeNode("4",[])
Tree.addChild(four)


print(Tree)