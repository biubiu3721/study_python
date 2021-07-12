# utf8-coding
"""
1. Create
2. Setwise operator
3. Update
4. Sort
"""

x= set("runoob") # iterable to set{}
y = set("google")
print("x, y ", x, y)
print("intersect", x & y)
print("union", x | y)
print("subtract", x - y)

x.update("c")
print("x.update('c')", x)

print(sorted(x, key=None, reverse=True))