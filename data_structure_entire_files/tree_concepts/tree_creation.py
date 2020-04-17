# Tree creation using linked list

class Node:

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self):
        self.root = None

    def insertion(self, new_node):
        if self.root:
            current = self.root_node
            parent = None
            while True:
                parent = current
        if self.root:
            if self.root.left:
                self.root.right = Node(new_node)
            else:
                self.root.left = Node(new_node)
        else:
            self.root = Node(new_node)

    def find_min(self):
        """ This will give min in BT """
        current = self.root
        while current.left:
            current = current.left
        
        return current

    def find_count(self):
        """ This will give count in BT """
        current = self.root
        cnt = 0
        while current.left:
            current = current.left
            cnt +=1
        
        return cnt

    def pre_order_traversal(self):
        """ The order of traversal is Root Left Right """
        if self.root:
            print(self.root.data, end="  ")
            pre_order_traversal(self.root.left)
            pre_order_traversal(self.root.right)
        else:
            print('The tree is empty')
    
    def in_order_traversal(self):
        """ The order of traversal is Left Root Right """
        if self.root:
            in_order_traversal(self.root.left)
            print(self.root.data, end = "   ")
            in_order_traversal(self.root.right)

    

'''
root = Node(1) 
root.left      = Node(2) 
root.right     = Node(3) 
root.left.left  = Node(4) 
root.left.right  = Node(5)
root.left.left.left = Node(7)
root.right.left = Node(6) 
#pre_order_traversal(root)
in_order_traversal(root)
'''

# Tree creation
# insertion node
# Deletion node
# Search
# Traversal
# deletion of tree

# Tree creation using array
# left child 2n and right child 2n+1
# Tree types BST, AVL , Red Black Tree, Syntax Tree
