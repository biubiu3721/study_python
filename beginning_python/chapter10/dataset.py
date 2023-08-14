# -*- coding:utf-8 -*-
"""
Project   : study_python
File Name : dataset.py
Author    : Focus
Date      : 8/3/2023 5:52 PM
Keywords  : 
Abstract  :
Param     : 
Usage     : py dataset.py
Reference :
"""
# import numpy as np
# import matplotlib.pyplot as plt
# import sys

import sys, shelve


def store_person(db):
    pid = input("Enter unique ID number: ")
    person = {}
    person["name"] = input("Enter name: ")
    person["age"] = input("Enter age: ")
    person["phone"] = input("Enter phone nuber: ")
    db[pid] = person


def lookup_person(db):
    pid = input("Enter ID Number: ")
    field = input("what would you like to know? (name, age, phone) ")
    field = field.strip().lower()
    print(field.capitalize() + ": " + db[pid][field])


def print_help():
    print("The available commands are: ")
    print("store: Stores information about a person")
    print("lookup: Looks up a person from ID number")
    print("quit: Save change and exit")
    print("? : print this message")


def enter_command():
    cmd = input("Enter command (? for help): ")
    cmd = cmd.strip().lower()
    return cmd


def main():
    database = shelve.open("./database.dat")
    try:
        while True:
            cmd = enter_command()
            if cmd == "store":
                store_person(database)
            elif cmd == "lookup":
                lookup_person(database)
            elif cmd == "?":
                print_help()
            elif cmd == "quit":
                return
    finally:
        database.close()

if __name__ == '__main__': main()
