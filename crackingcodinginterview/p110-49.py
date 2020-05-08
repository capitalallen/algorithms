class Node:

    def __init__(self, item):
        self.right = None
        self.left = None
        self.val = item
        self.parent = None

    def __str__(self):
        return '('+str(self.left)+':L ' + "V:" + str(self.val) + " R:" + str(self.right)+')'

    def sequences(self,node1,node2):
       pass 

node = Node(5)
node.left = Node(3)
node.right = Node(10)
node.left.parent = node
node.right.parent = node

node.left.left = Node(1)
node.left.right = Node(4)
node.left.left.parent = node.left
node.left.right.parent = node.left

node.right.left = Node(7)
node.right.right = Node(11)
node.right.left.parent = node.right
node.right.right.parent = node.right