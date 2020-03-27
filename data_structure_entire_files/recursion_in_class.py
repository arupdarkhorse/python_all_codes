'''
class Testval:

    def __init__(self, num):
        self.num = num
        #self.lis = lis

    def recur(self,):
        if self.num:
            print(self.num)
            self.num = self.num -1
            self.recur()

arup = Testval(5)
arup.recur()

class Testval:
    """ Recursion implementation inside class """

    def __init__(self, num):
        self.num = num
        #self.lis = lis

    def recur(self, num1):
        if num1:
            print(self.num)
            self.num = self.num -1
            self.recur(num1-1)
    
    def recurs(self):
        def inner_recur(number):
            if number:
                print(number)
                return inner_recur(number-1)
        num2 = self.num
        inner_recur(num2)

arup = Testval(5)
arup.recur(3)
arup.recurs()

'''
class Node:

    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    '''
    # Testing declaring outside init
    def __init__(self):
        self.head = None
    
    
    # using new pointer cur
    def insertion(self, new_node):
        """ using recursion """
        if not self.head:
            self.head = Node(new_node)
            self.cur = self.head    
        else:
            if self.cur:
                self.cur = self.cur.next
                self.insertion(new_node)
            else:
                self.cur = Node(new_node)
    '''
    '''
    # using two pointers
    def __init__(self):
        self.head = None
        self.cur = self.head
    
    
    def insertion(self, new_node):
        """ using recursion """
        if self.cur:
            self.cur = self.cur.next
            self.insertion(new_node)
        else:
            self.cur = Node(new_node)
            print(self.head)
    '''
    def __init__(self):
        self.head = None

    def insertion(self, new_node):
        def recur(cur):
            if cur.next:
                cur = cur.next
                recur(cur)
            else:
                cur.next = Node(new_node)
        if not self.head:
            self.head = Node(new_node) 
        else:
            current = self.head
            recur(current)
    
    def traversal(self):
        def recur(cur):
            if cur:
                print(cur.data)
                cur = cur.next
                recur(cur)

        current = self.head
        recur(current)
            


arup = LinkedList()
arup.insertion(1)
arup.insertion(2)
arup.insertion(3)
arup.insertion(4)
arup.insertion(5)
arup.insertion(6)
arup.insertion(7)

arup.traversal()
