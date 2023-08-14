# -*- coding:utf-8 -*-
"""
Project   : study_python
File Name : chapter9
Author    : Focus
Date      : 6/25/2023 10:53 AM
Keywords  : 
Abstract  :
Param     : 
Usage     : py chapter9
Reference :
"""
# import numpy as np
# import matplotlib.pyplot as plt
# import sys


# class Bird:
#     def __init__(self):
#         self.hungry = True
#     def eat(self):
#         if self.hungry:
#             print("Aaaah ...")
#             self.hungry = False
#         else:
#             print("No, thanks!")
#
#
# b = Bird()
# b.eat()
# b.eat()
#
#
# class SongBird(Bird):
#     def __init__(self):
#         self.sound = "Squawk!"
#         super().__init__()
#         super(SongBird, self).__init__()
#
#     def sing(self):
#         print(self.sound)
#
#
# sb = SongBird()
# sb.sing()
# sb.eat()
#
#
# def check_index(key):
#     if not isinstance(key, int): raise TypeError
#     if key < 0: raise IndexError
#
#
# class ArithmeticSequence:
#     def __init__(self, start=0, step=1):
#         self.start = start
#         self.step = step
#         self.changed = {}
#
#     def __getitem__(self, key):
#         check_index(key)
#         try: return self.changed[key]
#         except KeyError:
#             return self.start + key * self.step
#
#     def __setitem__(self, key, value):
#         check_index(key)
#         self.changed[key] = value
#
#
# s = ArithmeticSequence(1, 2)
# print(s[4])
# s[4] = 2
# print(s[4])
# print(s[5])
# del s[4]

#
# class CounterList(list):
#     def __init__(self, *args):
#         super().__init__(*args)
#         self.counter = 0
#     def __getitem__(self, index):
#         self.counter += 1
#         return super().__getitem__(index)
#
#
# cl = CounterList(range(10))
# print(cl)
# cl.reverse()
# print(cl)
# del cl[3:6]
# print(cl)
# print(cl.counter)
# print(cl[4] + cl[2])
# print(cl.counter)

"""
9.5.1
"""

# class Rectangle:
#     def __init__(self):
#         self.width = 0
#         self.height = 0
#     def set_size(self, size):
#         self.width, self.height = size
#     def get_size(self):
#         return self.width, self.height
#     size = property(get_size, set_size)
#
#
# r = Rectangle()
# r.width = 10
# r.height = 5
# print(r.size)
# r.size = 150, 100
# print(r.width)


# class MyClass:
#     def smeth():
#         print("This is a static method")
#     smeth = staticmethod(smeth)
#     def cmeth(cls):
#         print("This is a class method", cls)
#     cmeth = classmethod(cmeth)
#
#
# MyClass.smeth()
# MyClass.cmeth()
#
#


# class Rectangle:
#     def __init__(self):
#         self.width = 0
#         self.height = 0
#     def __setattr__(self, name, value):
#         if name == "size":
#             self.width, self.height = value
#         else:
#             self.__dict__[name] = value
#     def __getattr__(self, name):
#         if name == "size":
#             return self.width, self.height
#         else:
#             raise AttributeError()

"""
9.6
"""

class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a
    def __iter__(self):
        return self


fibs = Fibs()
print(next(fibs))
print(next(fibs))
print(next(fibs))
print(fibs.a, fibs.b)
for f in fibs:
    if f > 1000:
        print(f)
        break


it = iter([1, 2, 3])
print(next(it))
print(next(it))


"""
9.6.2
"""

class TestIterator:
    value = 0
    def __next__(self):
        self.value += 1
        if self.value > 10: raise StopIteration
        return self.value
    def __iter__(self):
        return self

ti = TestIterator()
print(list(ti))


nested = [[1, 2], [3, 4], [5]]

def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element

for num in flatten(nested):
    print(num)

print(list(flatten(nested)))

g = ((i + 2) ** 2 for i in range(2, 27))
print(next(g))
print(next(g))

print(sum(i ** 2 for i in range(10)))


def flatten(nested):
    try:
        try: nested + ""
        except TypeError: pass
        else: raise TypeError

        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested


print(list(flatten([[[1], 2], 3, 4, [5, [6, 7]], 8])))
print(list(flatten(["foo", ["bar",  ["barz"]]])))


def simple_generator():
    yield 1

print(simple_generator())
print(list(simple_generator()))


def repeator(value):
    while True:
        new = (yield value)
        if new is not None: value = new

r = repeator(42)
print(next(r))
r.send("Hello World")



def flatten(nested):
    result = []
    try:
        try: nested + ""
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                result.append(element)
    except TypeError:
        result.append(element)
    return result


def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False

# set last queen
def queens(num, state):
    if len(state) == num - 1:
        for pos in range(num):
            if not conflict(state, pos):
                yield pos


