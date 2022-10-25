# coding:utf-8
"""
Li = [200, 390, ]
"""


class Node:
    """node of single List"""

    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList(object):
    """single link list"""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """ is empty"""
        return self.__head == None

    def length(self):
        """ length of list """
        l = 0
        cur = self.__head
        while cur != None:
            l = l + 1
            cur = cur.next
        return l

    def travel(self):
        """ travel """
        cur = self.__head
        while cur != None:
            print(cur.item, end=" ")
            cur = cur.next
        print(" ")

    def add(self, item):
        """ add at head """
        node = Node(item)
        node.next = self.__head
        self.__head = node
        pass

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

        while cur.next != None:
            cur = cur.next
        cur.next = node

    def insert(self, pos, item):
        """ insert at specific position
        :param pos start from 0. new item is at a[pos]
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
        pre = self.__head
        """
        skip  [0, pos - 1]
        """
        while count < pos - 1:
            count = count + 1
            pre = pre.next

        node.next = pre.next
        pre.next = node

    def remove(self, item):
        """ remove based on value"""
        cur = self.__head
        pre = None
        while cur != None:
            if cur.item == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next

    def __remove(self, item):
        """ remove based on value"""
        cur = self.__head
        pre = None
        while cur != None:
            if cur.item == item:
                pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next


    def search(self, item):
        """ search whether item is in this list."""
        cur = self.__head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False




print("start")

if __name__ == "__main__":
    ll = SingleLinkList()
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
