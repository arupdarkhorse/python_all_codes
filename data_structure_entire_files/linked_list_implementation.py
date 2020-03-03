
'''
# with normal init method
class Node:
    """ This class will contain value of node and pointer to the next node """
    def __init__(self, data=None):
        self.data = data
        self.next = None
'''
def Node_init(self, data):
    self.data = data
    self.next = None
Node = type('Node', (), {'__init__' : Node_init})

class SingleLinkedList():
    """ This class will contains various operation performed with linked list """
    def __init__(self):
        self.head = None
    
    def insert_node_to_list(self, new_node):
        cur = self.head
        if self.head:
            while cur.next:
                cur = cur.next
            cur.next = Node(new_node)
        else:
            self.head = Node(new_node)

    def traverse_list(self):
        cur = self.head
        while cur:
            print(f"{cur.data}\t")
            cur = cur.next

    def insert_node_after_giv_node(self, giv_node, new_node):
        """ this will insert new node after a given node """
        new_node = Node(new_node)
        cur = self.head
        while cur:
            if cur.data == giv_node:
                next_node = cur.next
                cur.next = new_node
                new_node.next = next_node
                return
            cur = cur.next
        print(f"Given node {giv_node} does not exist in the linked list")


'''
Linked list sample example testing       
a = Node(3)
b = Node(4)
c = Node(5)
a.next = b
b.next = c
print(a.next.next.data)
'''
mylist = SingleLinkedList()
for i in [2,3,4]:
    mylist.insert_node_to_list(i)
mylist.traverse_list()
mylist.insert_node_after_giv_node(3,5)
mylist.traverse_list()
