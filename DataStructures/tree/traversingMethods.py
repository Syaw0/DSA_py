import math
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class Tree:
    def __init__(self, tree):
        self.tmpTree = tree
        self.tree = []
        self.tmp = []
        self.makeTree()

    def makeTree(self):
        for item in self.tmpTree:
            tmpNode = Node(item)
            self.tree.append(tmpNode)

        for index in range(0, len(self.tree) - 1):
            left = index * 2 + 1
            right = index * 2 + 2
            if left < len(self.tmpTree):
                self.tree[index].left = self.tree[left]
            if right < len(self.tmpTree):
                self.tree[index].right = self.tree[right]

    def inOrderTraverse(self, root=0, callback=None):
        if root == 0:
            root = self.tree[0]

        if root.left != None:
            self.inOrderTraverse(root.left, callback)

        # * add an callback to use traverse feature!!
        if callback != None:
            callback(root)

        self.tmp.append(root.value)

        if root.right != None:
            self.inOrderTraverse(root.right, callback)

    def preOrderTraverse(self, root=0):
        if root == 0:
            root = self.tree[0]

        self.tmp.append(root.value)

        if root.left != None:
            self.preOrderTraverse(root.left)

        if root.right != None:
            self.preOrderTraverse(root.right)

    def postOrderTraverse(self, root=0):
        if root == 0:
            root = self.tree[0]
        if root.left != None:
            self.postOrderTraverse(root.left)

        if root.right != None:
            self.postOrderTraverse(root.right)
        self.tmp.append(root.value)

    def isFullBinary(self): 
        # * full binary tree have Odd number and we must check for number of internal nodes
        # * and every of internal nodes must have 2 child
        numberOfInternalNodes = 0
        numberOfExternalNodes = 0
        wholeNodes = len(self.tree)
        validity = True
        def checkNode(node):
            nonlocal numberOfExternalNodes,numberOfInternalNodes,validity # to tell python these aren't new variables...
            if node.left != None and node.right != None:
                numberOfInternalNodes += 1
            elif node.left != None or node.right != None:
                validity = False
            else :
                numberOfExternalNodes +=  1
        self.inOrderTraverse(0,checkNode)
        
        if (wholeNodes - 1) / 2 == numberOfInternalNodes and validity == True:
            if (wholeNodes + 1) / 2 == numberOfExternalNodes:
                print("full binary")
        else:
            print("its not full binary tree")


    def isPerfectBinary(self):
        # * perfect binary tree has number of odd nodes and every internal node has 2 child
        # * and every leaf node must be in the same level
        wholeNodes = len(self.tree)
        TreeLevel = math.frexp(wholeNodes)[1]
        numberOfNodesInLevel = (1 << TreeLevel) - 1
        if numberOfNodesInLevel == wholeNodes:
            print("yes its a perfect binary tree")
        else:
            print("no its not perfect binary")

    def isCompleteBinary(self, node=0, index=-1):
        tmpNode = node
        if node == 0:
            tmpNode = self.tree[0]
            index = 0
        if tmpNode == None:
            return True
        
        if index >= len(self.tree):
            return False

        return (self.isCompleteBinary(tmpNode.left, index * 2 + 1) 
        and  self.isCompleteBinary(tmpNode.right, index * 2 + 1))


x = Tree([1,2,3,4,5,6,7,8,9,23,11,12,13,14,15])
print(x.isCompleteBinary())
# x.isPerfectBinary()
# x.isFullBinary()