# -*- coding:utf-8 -*-
"""
Project   : grammar
File Name : super
Author    : Focus
Date      : 10/25/2022 10:53 AM
Keywords  : 
Abstract  :
    super() 会按照self.__class__.__mro__的顺序仅调用父类的同名函数。
    super(type, obj) 中的type默认本类， obj 默认为起始类的对象。
Param     : 
Usage     : py super
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
import sys


class A:
    def __init__(self):
        print(self)
        #print("打印属性 a")
    def bark(self):
        print("bark: A")


class B(A):
    def __init__(self):
        print(self)
        print("打印属性 b")
        #super().__init__()  # super() 等同于 super(B, self)
    def bark(self):
        print("bark: B")

class C(A):
    def __init__(self):
        print(self)
        print("打印属性 c")
        #super().__init__()  # super() 等同于 super(C, self)
    def bark(self):
        print("bark: C")


class D(B, C):
    def __init__(self):
        print(self)
        print(self.__class__.__mro__)
        print("打印属性 d")
        super(D, self).__init__()
    def bark(self):
        print("bark: D")
        super().bark()

d = D()
d.bark()



class A(object):
    def __init__(self):
        print(self.__class__.__mro__)

    def bark(self):
        print("I'm A")
        super(A, self).bark()

class B(object):
    def bark(self):
        print("I'm B")


class C(A, B):
    def bark(self):
        print("I'm C")
        super(C, self).bark()

def case1():
    d = D()
    d.bark()


def case2():
    c = C()
    c.bark()


if __name__ == '__main__':
    case1()
    case2()
