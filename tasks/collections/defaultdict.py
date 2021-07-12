from collections import defaultdict

"""
defaultdict
"""
# 1. defaultdict basic
dic = defaultdict(dict);
dic["k1"].update({"asdsa": "123"})
print(dic)

a = 3.5
print(a, int(a))
print(dic)