#coding=utf-8


from collections import Counter

"""
1. Test Case
"""
# dict is element * item.
str = "abcbcaccbbad"
li = ["a","b","c","a","b","b"]
d = {"1":2, "3":1, "17":3}

"""
2. Build dict order by Frequence.
   Support input:
       1. list.
       2. dict.
"""
# Counter: Get element num, and return dict.
print("Counter(str): ", Counter(str)) # return a Counter contain a map ordered by frequence.
print("COunter(li): ", Counter(li)) # return a Counter contain a map ordered by frequence.
print("Counter(d): ", Counter(d)) # return a Counter contain a map ordered by frequence.

"""
3. method
"""
d1 = Counter(str)
# 3.1 most_common(int)
print("d1.most_common(2)", d1.most_common(2)) # return a dict ordered by frequence of second item.

#3.2 eltment . a:2, b:3 -> aabbb
print("d1.eltments()", d1.elements()) # iter point to head of the dict
print("sorted(d1.elements())", sorted(d1.elements())) # return a dict
print('("".join(d1.elements())): ',"".join(d1.elements()))  # return a string.
print("next iter", next(d1.elements())) # return the first element.

#3.3
d2 = Counter(d)
print("d2:", d2)
print("d2.elements()", d2.elements())
print("return value key", sorted(d2.elements()))


#3.4 update
print("4. update")
print("d1", d1)
d1.update("a")
print(d1)
