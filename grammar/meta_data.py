# -*- coding:utf-8 -*-
"""
Project   : study_python
File Name : meta_data.py
Author    : Focus
Date      : 11/13/2022 5:37 PM
Keywords  : 
Abstract  :
    meta data is the default attribute of a class, including
          ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
           '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
            '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__',
            '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
            '__sizeof__', '__str__', '__subclasshook__', '__weakref__',]
    most of the time, you don't need to change any of them.
    * what is function.func_code?
Param     :
Usage     : py meta_data.py
Reference :
"""
# import numpy as np
# import matplotlib.pyplot as plt
# import sys


def plus(a):
    a = a + 1
    return a

#print(dir(plus))


import fnmatch as m

print(m.__doc__.splitlines()[0])
print(m.__name__)
print(m.__file__)
print(m.__dict__.items())


class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def miao(self):
        print("miao: my name is ", self.name)


Cat1 = Cat("kitty", 3)


print(Cat.__doc__)
print(Cat.__module__)
print(Cat.__bases__)
print(Cat.__dict__)
print(Cat1.__dict__)
print(Cat1.__class__)

im = Cat.miao

import inspect

im = Cat1.miao
if inspect.isroutine(im):
    im()

