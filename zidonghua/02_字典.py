

dict = {"ele1" : [1, 2], 
        "ele2" : "你好", 
        "ele3" : 1, 
        "ele4" : 1.0, 
        "ele5" : {"A", "B", "C"}}

print(dict)
print(len(dict))
print(type(dict))


#添加元素key
dict["ele6"] = "a"
print(dict)

#pop
dict.pop("ele6")
print(dict)

#popitems--默认删除最后一对key/value
dict.popitem()
print(dict)


#clear() ---清空
# dict.clear()
# print(dict)

#修改key/value
# dict["ele1"] = "hello"
# print(dict)

#取出所有的key
for key in dict.keys():
    print(key)

#取出所有的value
for value in dict.values():
    print(value)

#同时取出key和value
for key, value in dict.items():
    print(key, value)