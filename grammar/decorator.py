"""
Add decorator to a function means
     run decorator while the input is the function.
Ref:
    https://zhuanlan.zhihu.com/p/51035016
"""

import datetime

__DEBUG__ = True

"""

decorator equalt to define the function and run decorator(func)
"""
def log(func):
    if __DEBUG__:
        print("Function start at ", datetime.datetime.now())
    func()
    if __DEBUG__:
        print("Function end at ", datetime.datetime.now())
"""

decorator equalt to define the function, run decorator(func) and return to test
"""
def log2(func):
    def wrapper():
        if __DEBUG__:
            print("function start at ", datetime.datetime.now())
        func()
        if __DEBUG__:
            print("function start at ", datetime.datetime.now())
    return wrapper


@log2
def test():
    print("test")
    test_lst = []
    for i in range(100):
        test_lst.append(i)


def log3(func):
    def wrapper(*args, **kwargs):
        if __DEBUG__:
            print("function start at ", datetime.datetime.now())
        func(*args, **kwargs)
        if __DEBUG__:
            print("function end at", datetime.datetime.now())
    return wrapper
@log3
def test1(a, b):
    print("test")
    test_lst = []
    for i in range(a):
        test_lst.append(i * b)


test1(1, 2)


from functools import wraps


class aop(object):
    def __init__(self, aop_test_str):
        self.aop_test_str = aop_test_str
    def __call__(self, func):
        print("aop.__call__ is running")
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Before " + self.aop_test_str)
            func(*args, **kwargs)
            print("after " + self.aop_test_str)
        return wrapper
"""
temp = aop("ppppp")
hi = temp(hi)
"""
@aop("pppppp")
def hi():
    print(hi)


class sub_aop(aop):
    def __init__(self, sub_aop_str, *args, **kwargs):
        self.sub_aop_str = sub_aop_str
        super(sub_aop, self).__init__(*args, **kwargs)

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('before ' + self.sub_aop_str)
            super(sub_aop, self).__call__(func)()
            print('after ' + self.sub_aop_str)

        return wrapper


@sub_aop('ssssss', 'pppppp')
def hello():
    print('hello')

hello()

