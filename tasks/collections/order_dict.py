from collections import OrderedDict

"""
Ordered Dict will sort by input order of the keys.
"""
# 1. 

dic1 = dict()
dic1["a"] = "123"
dic1["d"] = "jjj"
dic1['c'] = '394'  
dic1['b'] = '999'  
dic1['a'] = '321' # fail to be added, but no error raised.
print("dict1: ", dic1)
# order
dic1_key_list = []
for k in dic1.keys():
    dic1_key_list.append(k)
dic1_key_list.sort() # sort by alphabetical order.
for key in dic1_key_list:
    print("dic dictionary sort result is: ", key, dic1[key])
# 2. OrderDict
dic2 = OrderedDict() # order by 
dic2["a"] = "123"
dic2["d"] = "jjj"
dic2["c"] = "abc"
dic2["b"] = "999"

for k, v in dic2.items():
    print("Ordered Dict: ", k, v)


