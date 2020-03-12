'''
class A:
    """ class creating normally"""
    pass
x = A()
print(type(x))
# class creation using type
B = type("A", (), {})
y = B()
print(type(y))
# syntax of type class = type(classname, superclasses, attributedict)
# __call__ method call __new__ and then __init__
# this means type.__new__(typeclass, classname, superclasses, attributedict)
# then type.__init__(cls, classname, superclasses, attributedict)
# new method creates and returns new class object, and after this __init__ method initializes the newly created object
# Another example of type class
class Robot:
    counter = 0
    def __init__(self, name):
        self.name = name
    def sayhello(self):
        
        return f"Hi, my name is {self.name}"
y = Robot('Arup')
print(y.sayhello(), y.name)
def Rob_init(self, name):
    self.name = name
Robot2 = type("Robot",
                (),
                {"counter" : 0,
                "__init__" : Rob_init,
                "sayhello" : lambda self : f"Hi, my name is {self.name}"
                })
x = Robot2('Gauss')
print(x.sayhello(), x.name)
print(x.__dict__)
print(y.__dict__)
'''

'''
# slots in python
""" slots are used for stoping the creation of object dinamically """
class A:
    pass

x = A()
x.a = 66
x.b = "arup here"
print(x.__dict__)
# But we can't do the same for predefined int, str like object. We'll get attribute error
x = 42
x.t = 56
print(x.__dict__)
# we can the same feature using __slots__
class Arup:
    
    __slots__ = ['val', 'number']

    def __init__(self, val, number):
        self.val = val
        self.number = number

arup1 = Arup(23, 45)
arup1.ty = 'wiw'
'''
