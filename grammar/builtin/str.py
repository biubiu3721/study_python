# -*- coding:utf-8 -*-
"""
Project   : projects
File Name : str.py
Author    : Focus
Date      : 3/3/2022 3:20 PM
Keywords  : 
Abstract  :
            1. split
            2. join
            3. modify
            4. codec
            5. format
            6. method
               center
Param     : 
Usage     : py str.py
Reference :
"""
# import numpy as np
# import matplotlib.pyplot as plt
# import sys

def join2():
    "join".center(50, "*")
    seq = ['1', '2', '3', '4', '5']
    sep = "+"
    sep.join(seq)
    print(sep.join(seq))

def test6_center():
    """

    """
    print("The middle by Jimmy Eat world".center(39))
    print("The middle by Jimmy Eat world".center(39, "*"))
def test6_find():
    print('With a moo-moo here, and a moo-moo there'.find('moo'))
    title = "Monty Python's Flying Circus"
    print(title.find("Monty"))
    print(title.find("Python"))
    print(title.find("Flying"))
    print(title.find("Zirquss"))
    subject = "$$$ Get rich now!!! $$$"
    print(subject)
    print(subject.find("$$$"))
    print(subject.find("$$$", 1))
    print(subject.find("!!!"))
    print(subject.find("!!!", 1, 17)) # = clip(subject, 1, 17).find("!!!")
def test6_rfind():
    subject = "$$$ Get rich now!!! $$$"
    print(subject)
    print("rfind".center(100, "*"))
    print(subject.rfind("$$$"))
def test6_index():
    "index".center(40, "*")
    str1 = "this is string example....wow!!!"
    str2 = "exam"

    print(str1.index(str2))
    print(str1.index(str2, 10))
    print(str1.index(str2, 40))
def test6_startswith():
    print("startswith".center(40, "*"))
    str1 = "this is string example....wow!!!"
    str2 = "this"

    print(str1.startswith("this"))
    print(str1.startswith("is", 5))
    print(str1.startswith("is"))
if __name__ == "__main__":
    test6_center()
    test6_find()
    test6_rfind()
    #test6_index()
    test6_startswith()
    join2()

