# -*- coding:utf-8 -*-
"""
Project   : app
File Name : txt_to_mat.py
Author    : FAp
Date      : 3/3/2022 7:05 PM
Keywords  : 
Abstract  :
Param     : 
Usage     : py txt_to_mat.py
Reference :
"""
# import numpy as np
# import matplotlib.pyplot as plt
# import sys

def txt_to_mat(filename = "./data.txt"):
    mat = []
    with open(filename) as f:
        lines = f.readlines()
        lines = [line.replace(",", " ") for line in lines]
        lines = [line.strip(" \n") for line in lines]
        print("lines", lines)
        for line in lines:
            print(line)
            mat = mat +  line.split()
        print(mat)
    mat = [int(i) for i in mat]
    print(mat)
    return mat

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def is_same(self, new_pt):
        if self.x == new_pt.x and self.y == new_pt.y:
            return True
        else:
            return False


class c_line:

    def __init__(self, pt0, pt1):
        self.head = pt0
        self.tail = pt1
    def print(self):
        print("a cline".center(30, "*"))
        print("pt0: ", self.head.x, self.head.y)
        print("pt1: ", self.tail.x, self.tail.y)


class c_curve:

    def __init__(self, line0):
        self.head = line0.head
        self.tail = line0.tail
        self.lines = []
        if isinstance(line0, c_line):
            self.lines.append(line0)


    def print(self):
        print("a curve".center(50, "*"))

        print("head: ", self.head.x, self.head.y)
        print("head: ", self.tail.x, self.tail.y)
        print("has lines: ", len(self.lines))
        for idx in range(len(self.lines)):
            self.lines[idx].print()

    def merge(self, tmp_line):
        if isinstance(tmp_line, c_line):
            self.lines.append(tmp_line)
        else:
            self.lines += tmp_line.lines

    def update(self, new_line):
        """
        head
        tail
        """
        print("updating: ....")
        self.print()
        new_line.print()
        if self.head.is_same(new_line.head):
            self.head = new_line.tail
            self.lines.append(new_line)
            return True
        print("matching failed 1")

        if self.head.is_same(new_line.tail):
            self.head = new_line.head
            self.merge(new_line)
            return True
        print("matching failed 2")

        if self.tail.is_same(new_line.head):
            self.tail = new_line.tail
            self.merge(new_line)
            return True
        print("matching failed 3")

        if self.tail.is_same(new_line.tail):
            self.tail = new_line.head
            self.merge(new_line)
            return True
        print("matching failed 4")

        return False

def match_curves(curves):
    match_list = []
    bad_curves = []
    for i in range(len(curves)):
        for j in range(len(curves)):
            if i < j:
                if curves[i].update(curves[j]):
                    match_list.append((i, j, True))
                    bad_curves.append(curves[j])
    print(match_list)

    for i in range(len(bad_curves)):
        print("i", i)
        bad_curves[i].print()
        curves.remove(bad_curves[i])
    return len(match_list)



if __name__ == "__main__":
    print("start in main")
    mat = txt_to_mat("./data.txt")

    curves = []
    lines = []
    for line_idx in range(len(mat) // 4):
        pt0 = point(mat[line_idx * 4], mat[line_idx * 4 + 1])
        pt1 = point(mat[line_idx * 4 + 2], mat[line_idx * 4 + 3])
        line0 = c_line(pt0, pt1)
        line0.print()
        lines.append(line0)
    curves.append(c_curve(lines[-1]))
    lines.pop()
    print(len(curves), len(lines))
    rounds = 0
    while len(lines ) > 0 and rounds < 64:
        print("round: ", rounds)
        rounds +=1
        matched = []
        for line in lines:
            matched = False
            for curve in curves:
                if curve.update(line):
                    print("matched".center(100, "#"))
                    lines.remove(line)
                    matched = True
                    break

            if not matched:
                tmp_curve = c_curve(line)
                curves.append(tmp_curve)
                lines.remove(line)


    print("total curve num is: ", len(curves))
    while(match_curves(curves) > 0):
        print(len(curves))

    print("total curve num is: ", len(curves))


    for curve in curves:
        curve.print()
