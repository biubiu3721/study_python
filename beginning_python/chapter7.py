# -*- coding:utf-8 -*-
"""
Project   : study_python
File Name : chapter7.py
Author    : Focus
Date      : 6/20/2023 7:54 PM
Keywords  : 
Abstract  :
Param     : 
Usage     : py chapter7.py
Reference :
"""
# import numpy as np
# import matplotlib.pyplot as plt
# import sys
class test:
    def __init__(self,name,age):
        self.age = age
        self.name = name
    def __repr__(self):
        return "Class_Test[name="+self.name+",age="+str(self.age)+"]"

t = test("Zhou",30)

print(t)

def function():
    print("I don't")
class Person:

    def set_name(temp, name):
        temp.name = name
    def get_name(self):
        return self.name
    def greet(self):
        print("Hello world! I'm {}".format(self.name))
    def test():
        print("test")


foo = Person()
foo.set_name("Luke")
Person.greet(foo)
foo.test = function
foo.test()

class Secretive:

    def __inaccessible(self):
        print("Bet you can't see me ...")

    def accessible(self):
        print("The secret message is:")
        self.__inaccessible()

s = Secretive()
#s.__inaccessible()
print(s._Secretive__inaccessible())
# s.accessible()
# s._Secretive__inaccessbile()

class MemberCounter:
    members = 0
    def init(self):
        MemberCounter.members += 1


m1 = MemberCounter()
m1.init()
print(MemberCounter.members)
m2 = MemberCounter()
m2.init()
print(MemberCounter.members)

print(m1.members)
print(m2.members)
m1.members = "Two"
print(m1.members)
print(m2.members)
print(MemberCounter.members)


class Filter:

    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter):
    def init(self):
        self.blocked = ["SPAM"]

f = Filter()
f.init()
print(f.filter([1, 2, 3]))


s = SPAMFilter()
s.init()
print(s.filter(["SPAM", "SPAM", "SPAM", "SPAM", "eggs", "bacon"]))

print(issubclass(SPAMFilter, Filter))
print(issubclass(Filter, SPAMFilter))

print(SPAMFilter.__bases__)
print(Filter.__bases__)

s = SPAMFilter()
print(isinstance(s, SPAMFilter))
print(isinstance(s, Filter))
print(isinstance(s, str))

print(s.__class__)
print(type(s))

class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)


class Talker:
    def talk(self):
        print("Hi, my value is ", self.value)


class TalkingCalculator(Calculator, Talker):
    pass

tc = TalkingCalculator()
tc.calculate('1 + 2 * 3')
tc.talk()

print(hasattr(tc, 'talk'))
print(hasattr(tc, 'fnord'))
print(callable(getattr(tc, 'talk', None)))
print(callable(getattr(tc, 'fnord', None)))

setattr(tc, 'name', 'Mr. Gumby')
print(tc.name)
print(tc.__dict__)


import inspect
print(inspect.getmembers(tc))

from abc import ABC, abstractmethod

class Talker(ABC):
    @abstractmethod
    def talk(self):
        pass


class Knigget(Talker):
    pass


class Knigget(Talker):
    def talk(self):
        print("Ni")

Knigget()

class Herring:
    def talk(self):
        print("Blub.")

h = Herring()
print(isinstance(h, Talker))
Talker.register(Herring)
print(isinstance(h, Talker))
issubclass(Herring, Talker)

class Clam:
    pass

