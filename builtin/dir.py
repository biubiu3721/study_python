import numpy as np

"""
获取类或对象所有的函数名和变量名，返回一个list。 
"""

class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def miao(self):
        print("miao: my name is ", self.name)

Cat1 = Cat("kitty", 3)

print(dir(Cat))
print(dir(Cat1))

"""
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'miao']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'miao', 'name']

"""


print(hasattr(Cat, "__class__"))
print(getattr(Cat, "__class__"))
print(getattr(Cat, "__name__"))