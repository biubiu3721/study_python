"""
* 作用域

Python 中变量的访问权限取决于其赋值的位置，这个位置被称为变量的作用域。Python 的作用域共有四种，分别是：局部作用域（Local，简写为 L）、作用于闭包函数外的函数中的作用域（Enclosing，简写为 E）、全局作用域（Global，简写为 G）和内置作用域（即内置函数所在模块的范围，Built-in，简写为 B）。

变量在作用域中查找的顺序是 L→E→G→B，即当在局部找不到时会去局部外的局部找（例如闭包），再找不到会在全局范围内找，最后去内置函数所在模块的范围中找。

分别在 L、E、G 范围内定义的变量的例子如下：
global_var = 0 #全局作用域
def outer():
enclosing_var = 1 #闭包函数外的函数中
def inner():
local_var = 2 #局部作用域

内置作用域则是通过 builtins 模块实现的，可以使用以下代码查看当前 Python 版本的预定义变量：
import builtins
dir(builtins)



"""


"""
6.3.1
"""


def square(x):
    """Calculates the square of the number x."""
    return x * x


print(square.__doc__)
help(square)

"""
6.3.2
"""


def test():
    print("This is printed")
    return
    print("This is not")


x = test()


"""
6.4
"""


def try_to_change(n):
    n = "Mr. Gumby"


name = "Mrs. Entity"
try_to_change(name)
print(name)


def change(n):
    """
    changed
    """
    n[0] = "Mr. Gumby"


names = ["Mrs. Entity", "Mrs. Thing"]
change(names)
print(names)


names = ["Mrs. Entity", "Mrs. Thing"]
n = names
n[0] = "Mr. Gumby"
print(names)


names = ["Mrs. Entity", "Mrs. Thing"]
n = names[:]
print(n is names)
print(n == names)

n[0] = "Mr. Gumby"
print(n)
print(names)


def init(data):
    data["first"] = {}
    data["middle"] = {}
    data["last"] = {}


storage = {}
init(storage)
print(storage)


def lookup(data, label, name):
    return data[label].get(name)


lookup(storage, "middle", "Lie")


def store(data, full_name):
    names = full_name.split()
    if len(names) == 2: names.insert(1, "")
    labels = "first", "middle", "last"
    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]

MyNames = {}
init(MyNames)
store(MyNames, 'Magnus Lie Hetland')
ret = lookup(MyNames, 'middle', "Lie")
print(ret)


"""
6.4.4
"""


def print_params(*param):
    print(param)


print_params("testing")
print_params(1, 2, 3)


def print_params_2(title, *params):
    print(title)
    print(params)


print_params_2("Params: ", 1, 2, 3)
print_params_2("Nothing: ", )


def in_the_middle(x, *y, z):
    print(x, y, z)


in_the_middle(1, 2, 3, 4, 5, 6, z=7)


def print_params_3(**params):
    print(params)


print_params_3(x=1, y=2, z=3)


def print_params_4(x, y, z=3, *pospar, **keypar):
    print(x, y, z)
    print(pospar)
    print(keypar)


print_params_4(1, 2, 3, 4, 5, 6, 7, foo=1, bar=2)


"""
6.4.5
"""

def add(x, y):
    return x + y


params = (1, 2)
print(add(*params))


def hello_3(name, greeting):
    print(greeting, name)


params = {'name': "Sir Robin", 'greeting': "Well met: "}
hello_3(**params)


"""
6.4.6
"""

def story(**kwds):
    print(kwds)
    print(kwds["job"])
    print(kwds["name"])

params = {'name':'python'}
story(job="genius", **params)



"""
6.6.1
"""

def factorial(n):
    result = n
    for i in range(1, n):
        result *= i
    return result  


def factorial_(n):
    if n == 1:
        return 1
    else:
        return n * factorial_(n - 1)      


def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)
    

def search(sequence, number, lower=0, upper=None):
    if  upper == None:
        upper = len(sequence) - 1
    if lower == upper:
        assert sequence[upper] == number
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)


seq = [34, 67, 8, 123, 4, 100, 95]

seq.sort()

print(seq)

print(search(seq, 34))
print(search(seq, 100))


print(list(map(str, range(10))))


def func(x):
    return x.isalnum()


seq = ["foo", "x41", "?!", "***"]
print(list(filter(func, seq)))


x = [72, 101, 108, 108]
from functools import reduce
print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))