# -*- coding:utf-8 -*-
"""
Project   : study_python
File Name : bilist.py
Author    : Focus
Date      : 5/6/2022 2:02 AM
Keywords  : 
Abstract  :
Param     : 
Usage     : py bilist.py
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
import sys

from list import SingleLinkList


class Node(object):
    """
    double link node
    """

    def __init__(self, item):
        """
        :param item:
        """
        self.item = item
        self.prev = None
        self.next = None


class DoubleLinkList(SingleLinkList):
    """

    """
    def add(self, item):
        """ add at head """
        node = Node(item)
        node.next = self.__head
        self.__head = node
        node.next.prev = node

    def append(self, item):
        """
          append in tail
              1. init
              2. if is emplty head = node
              3. find the last none and change None to node.
          inputs:
              item: item is a number, avoiding user to know the node structure.

        """
        cur = self.__head
        node = Node(item)
        if self.is_empty():
            self.__head = node
            return
        while cur.next is not None:
            cur = cur.next
        cur.next = node
        node.prev = cur

    def insert(self, pos, item):
        """ insert at specific position
        :param pos start from 0. new item is at a[pos]
        :param item
        """
        print("insert at: ", pos)
        if pos <= 0:
            self.add(item)
            return

        if pos > self.length() - 1:
            self.append(item)
            return

        count = 0
        node = Node(item)
        """
        skip  [0, pos - 1]
        """
        while count < pos - 1:
            count = count + 1
            cur = cur.next

        node.next = cur
        node.prev = cur.prev
        cur.prev.next = node
        cur.prev = node

    def remove(self, item):
        """ remove based on value"""
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                return
            else:
                pre = cur
                cur = cur.next


if __name__ == "__main__":
    print("start in main")
    ll = DoubleLinkList

    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.travel()

    ll.insert(-1, 9)
    ll.travel()
    ll.insert(3, 100)
    ll.travel()
    ll.insert(10, 200)
    ll.travel()
    ll.remove(100)
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()
