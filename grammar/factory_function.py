# -*- coding:utf-8 -*-
"""
Project   : study_python
File Name : factory_function.py
Author    : Focus
Date      : 11/13/2022 4:43 PM
Keywords  : 
Abstract  :
   对上级的所有变量都可以引用。
   对全局变量修改需要加global
   对上级局部变量修改需要加 nonlocal, 外部嵌套函数内的变量
Param     : 
Usage     : py factory_function.py
Reference :
"""
# import numpy as np
# import matplotlib.pyplot as plt
# import sys
x = 99

def f1():
    x = 88
    def f2():
        print(x)

    return f2

action = f1()
action()

def maker(n):

    k = 8

    def action(x):
        return x ** n + k

    return action

f = maker(2)

print(f)

print(f(4))


def test(num):

    in_num = num
    x_num = 1

    def nested(label):
        nonlocal in_num
        global x
        x += 1
        in_num += 1
        print(label, in_num, x)
    return nested

F = test(0)
F("a")
F("b")
F("c")


G = test(100)
G("mm")
