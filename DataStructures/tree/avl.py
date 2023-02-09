from binarySearch import BinarySearch
from binarySearch import Node
class AVL(BinarySearch):
    def __init__(self, arr):
        super().__init__(arr)
        self.tmpList =[]

    def balance(self):
        result = self.isBalancedBinary()
        print(result,'result')
        if result==True:
            return True
        node = self.tmpList[0]['node']
        nodeNum = self.tmpList[0]['num']
        print('im using this node ',node.value)
        parent = node.parent
        if parent ==None:
            if nodeNum > 0:
                self.rightRotation(node.left)
            else:
                self.leftRotation(node.right)
        else:
            if nodeNum > 0:
                if node.left.right !=None:

                    self.leftRotation(node.left.right)

                    self.rightRotation(node.left)
                else:
                    self.rightRotation(node.left)
            else:
                if node.right.left !=None:
                    self.rightRotation(node.right.left)
                    self.leftRotation(node.right)
                else:
                    self.leftRotation(node.right)
        print(self.tmpList)
        self.tmpList = []
        print(self.tmpList)
        self.balance()

    def rightRotation(self,node):
        parent = node.parent
        parent.left = node.right
        if node.right != None:
            node.right.parent=parent
        node.parent = parent.parent
        if parent.parent.left == parent:
            parent.parent.left = node
        else:
            parent.parent.right = node
        parent.parent = node
        node.right = parent

    def leftRotation(self,node):

        parent = node.parent
        parent.right = node.left
        if node.left != None:
            node.left.parent=parent
        node.parent = parent.parent
        if parent.parent.left == parent:
            parent.parent.left = node
        else:
            parent.parent.right = node
        parent.parent = node
        node.left = parent

    def isBalancedBinary(self, node = 0, height= 0):
        # * If the difference between the two sides of a node in a tree is equal to one
        # * we call this binary tree a balanced binary...

        if node == 0 :
            node = self.tree[0]
            height = NodeHeight()
        
        rightNodeHeight = NodeHeight()
        leftNodeHeight =NodeHeight()

        if node == None:
            return True
        
        # recursively call to check all the elements...
        l = self.isBalancedBinary(node.left , leftNodeHeight)
        r = self.isBalancedBinary(node.right , rightNodeHeight)

        height.height = max(leftNodeHeight.height, rightNodeHeight.height) + 1
        if abs(leftNodeHeight.height - rightNodeHeight.height <= 1):
            return l and r
        else:
            self.tmpList.append({"node":node,"num":leftNodeHeight.height - rightNodeHeight.height})
            return False

    def search(self,value,node=0):
        if node==0:
            node= self.tree[0]
        if node == None:
            return False
        if node.value == value:
            print('found ',node.value)
            return node.value
        
        if   value > node.value:
            return self.search(value,node.right)
        else:
            return self.search(value,node.left)
            
        
    def insert(self,value,node=0):
        if node==0:
            searchResult = self.search(value)
            if searchResult!=False :
                
                return 'the value exist'
            else:
                node = self.tree[0]
        
            
        
        if value>node.value:
            if node.right != None:
                self.insert(value,node.right)
            else:
                self.tree.append(value)
                node.right = Node(value)
                node.right.parent = node
                self.balance()
        else:
            if node.left != None:
                self.insert(value,node.left)
            else:
                self.tree.append(value)
                node.left = Node(value)
                node.left.parent = node
                self.balance()
        
        
        

class NodeHeight:
    def __init__(self):
        self.height = 0


x = AVL([23,34,10,4,11,44,55,19])
x.show()
print()
if x.balance() != True:

    x.show()

print(x.search(55),'isEXIST?')

x.insert(123)
x.insert(5)
x.insert(1)
x.insert(32)
x.insert(30)
x.show()