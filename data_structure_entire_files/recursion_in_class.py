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
            

'''
arup = LinkedList()
arup.insertion(1)
arup.insertion(2)
arup.insertion(3)
arup.insertion(4)
arup.insertion(5)
arup.insertion(6)
arup.insertion(7)

arup.traversal()
'''
# try using static method
# try using decorator
# try using loop for bulk insert
'''
i = 0
def fun1(num):
    
    j = 0
    if num>0:
        i = i + j
        fun1(num-1)   
    #return i
def fun2(n):
    i= 0
    if n>0:
        i = i+ fun1(n)
        fun2(n-1)
    return i

print(fun1(5))

def increase(n):
    if n == 1:
        return 1
    else:
        temp = increase(n-1)
        print(f"printing upper {temp}")
        temp = n + temp
        print(f"printing lower {temp}")
        return temp
        

print(increase(4))

def fib(n):
    if n<2:
        return n
    else:
        temp1 = fib(n-2)
        temp2 = fib(n-1)
        print(f"Two numbers are {temp1} and {temp2}")
        temp = fib(n-1) + fib(n-2)
        return temp
print(f"final result is {fib(6)}")

# using dynamic programming using dictionary
arr = {0 : 0, 1 : 1}
def fibonacci(num):
    if num in arr:
        return arr[num]
    else:
        temp = fibonacci(num-1) + fibonacci(num-2)
        arr[num] = temp
        return temp
fibonacci(5)
print(arr)
#using formula
fib(n) = ((5**1/2 + 1)/2)**n/5**1/2
'''

def fib(n):
    temp = 1 + 5**(1/2)
    print(round((((5**0.5) + 1)/2)**n/5**0.5))

fib(6)


