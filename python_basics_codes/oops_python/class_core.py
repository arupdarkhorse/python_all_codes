"""class core concepts """
# class attributes, instance attributes
class A:
    pass
    
A.brand = 'hector'
A.name = "Sonata"
x = A()
print(x.brand)
x.brand = 'Tata'
print(f"{x.brand}\t {A.brand}")
# give error
#print(x.value)
print(getattr(x, "value", 100))     # getattr for handing exception
x.value = 3_00_000
print(x.__dict__)

def fun1(x):
    """ using function attributes as counter, to count number of time a function gets executed """
    fun1.counter = getattr(fun1, "counter", 0) + 1
fun1.x = 23  
for i in range(10):
    fun1(i)
print(fun1.counter)
print(f"fun1 attributes {fun1.__dict__}")

# Difference between instance and reference(alias name) of class
x = A()
y = A()
y1 = y
print(y==y1)
print(x==y)


class Boy:

    __slots__ = ['name', 'age']
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
x = Boy('Arup', 23)
# Throw error
#x.classes = 'Seventh'
print(x.__class__.__dict__)

# method example
def hi(object):
    print(f"Hi I am {object.name}.")
class Robot:
    say_hi = hi
x = Robot()
x.name = 'Utkal'
x.say_hi
Robot.say_hi(x)
# Method is a function defined inside a class
# x is used here as a reference to the calling instance, which is generally called self i.e.
'''
def age_name(obj):
    return obj.name, obj.age
class Name:
    first_fun = age_name
self = Name()
self.name = "Hari"
self.age = 23

print(self.first_fun())
'''
# __init__ method get executed immediately once an instance has been created

class Robot:

    def __init__(self):
        print("init is executed")
a = Robot()

def set_val