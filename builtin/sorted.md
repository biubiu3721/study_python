# 1.描述

# 2.语法

```
sorted(iterable, cmp=None, Key=None, reverse=False)
```

1. 参数说明：

   * iterable -- 可迭代对象

   * cmp -- 比较的函数

   * key -- 用来比较的元素， 是一个函数

   * reverse -- 排序规则， True 为降序， False为升序

2. 返回值
   * 排好序的列表，是一个新列表

# 3.实例

```
a = [5,7,6,3,4,1,2]
b = sorted(a) 
```

```
L=[('b',2),('a',1),('c',3),('d',4)]
sorted(L, cmp=lambda x,y:cmp(x[1],y[1]))   # 利用cmp函数
#[('a', 1), ('b', 2), ('c', 3), ('d', 4)]
sorted(L, key=lambda x:x[1])               # 利用key
# >>> [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
```

```
 students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
 sorted(students, key=lambda s: s[2]) 
```

