'''
dict = {"k1":"v1","k2":"v2","k3":"v3"}
#1、请循环遍历出所有的key
#2、请循环遍历出所有的value
# 3、请在字典中增加一个键值对,"k4":"v4"
'''
_dict={"k1":"v1","k2":"v2","k3":"v3"}
for i in _dict:
    print(i," ",end="")
print()
for i in _dict:
    print(_dict[i]," ",end="")
print()
_dict.update({"k4":"v4"})
print(_dict)