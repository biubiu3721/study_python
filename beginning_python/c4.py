# -*- coding:utf-8 -*-
"""
Project   : study_python
File Name : c4
Author    : Focus
Date      : 4/11/2023 11:13 AM
Keywords  : 
Abstract  :
Param     : 
Usage     : py c4
Reference :
"""
# import numpy as np
# import matplotlib.pyplot as plt
# import sys

"""
4.1
"""

people = {
    "Alice": {
        "phone": "2341",
        "addr": "Foo drive 23",
    },
    "Beth": {
        "phone": "9102",
        "addr": "Bar street 32",
    },
    "Cecil": {
        "phone": "3158",
        "addr": "Baz avenue 90",
    },
}

labels = {
    "phone": "phone number",
    "addr": "address",
}

name = input("Name: ")

request = input("Phone number (p) or address(a)")

key = request

if request == "p":
    key = "phone"
if request == "a":
    key = "addr"

    
person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, "not available")

print("{}'s {} is {}.".format(name, label, result))

"""
4.2
"""

template = '''<html>
              <head><title>{title}</title></head>
              <body>
              <h1>{title}</h1>
              <p>{text}</p>
              </body>'''
data = {"title": "My Home Page", "text": "Welcome come to my home page!"}
print(template.format_map(data))


"""

"""



