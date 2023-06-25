# -*- coding:utf-8 -*-
"""
Project   : study_python
File Name : chapter8
Author    : Focus
Date      : 6/21/2023 4:36 PM
Keywords  : 
Abstract  :
Param     : 
Usage     : py chapter8
Reference :
"""
# import numpy as np
# import matplotlib.pyplot as plt
# import sys


class SomeCustomException(Exception):
    pass


# try:
#     x = int(input("Enter the first number: "))
#     y = int(input("Enter the second number: "))
#     print(x / y)
# except ZeroDivisionError:
#     print("The second number can't be zero")


# class MuffledCalculator:
#     muffled = False
#     def calc(self, expr):
#         try:
#             return eval(expr)
#         except ZeroDivisionError:
#             if self.muffled:
#                 print("Division by zero is illegal")
#             else:
#                 raise
#
# calculator = MuffledCalculator()
# calculator.calc("10 / 2")
# calculator.muffled = True
# calculator.calc("10 / 0")

# try:
#     1 / 0
# except ZeroDivisionError:
#     raise ValueError from None

# try:
#     x = int(input("Enter the first number: "))
#     y = int(input("Enter the second number: "))
#     print(x / y)
# except (ZeroDivisionError, TypeError, NameError, ValueError) as e:
#     print("your numbers was bogus.")
#     print(e)
#     print(type(e))

"""
8.3.5
"""

# try:
#     x = int(input("Enter the first number: "))
#     y = int(input("Enter the second number: "))
#     print(x / y)
# except:
#     print("something wrong happened.")


# x = None
#
# try:
#     x = 1 / 0
# finally:
#     print("cleaning up")
#     del x


# try:
#     1 / 0
# except NameError:
#     print("Unknow Variable")
# else:
#     print("That went well!")
# finally:
#     print



"""
8.4
"""
#
# def faulty():
#     raise Exception("Something is wrong")
#
#
# def ignore_exception():
#     faulty()
#
#
# def handle_exception():
#     try:
#         faulty()
#     except:
#         print("Exception handle")
#
#
# #ignore_exception()
# handle_exception()

"""
8.5
"""

#
# def describe_person(person):
#     print("Description of ", person['name'])
#     print("Age: ", person['age'])
#     if 'occupation' in person:
#         print("Occupation: ", person["occupation"])
#
#
# person = dict()
# person["name"] = "Throat"
# person["age"] = 42
# describe_person(person)


# def describe_person(person):
#     print("Description of ", person['name'])
#     print("Age: ", person['age'])
#     try:
#         print("Occupation: ", person["occupation"])
#     except KeyError:
#         pass
#
#
# person = dict()
# person["name"] = "Throat"
# person["age"] = 42
# describe_person(person)


"""
8.6
"""

from warnings import warn
# warn("I've got a bad feeling about this")

from warnings import filterwarnings
filterwarnings("ignore")
warn("Anyone out there")
filterwarnings("error")
warn("Something is very wrong!")

