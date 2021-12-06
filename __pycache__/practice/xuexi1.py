'''元组
a = (1,2,"哈哈","git","哈哈","git""哈哈","git""哈哈",False)
b = (a,"哈哈","xixi",3)
# print(a[1])
# print(a.count("哈哈"))
# print(a.index(2))
# print(b)
# print(b[-1])
# print(b[2])
# print(b[0][3])
print(a[0:2])
print(b[:2])
print(b[-3:-1])
print(b[-3:])
'''

'''数组
m = [1,2,3,4,5,"12","nihao","你好","你好"]
# m.append(9)
# print(m)
# print(m.index(2))
# print(m.count("你好"))
# m.insert(0,6)
# print(m)
# a = m.pop(0)
# print(m)
# b = m.pop(0)
# print(m)
# # print(a)
# # print(b)
# print(a + b)
# print(a - b)
i = ["tianjia","添加"]
m.extend(i)
print(m)
# m.clear()
# print(m)
# print(m + i)
m.remove("添加")
print(m)
'''


# a = {"name":"张三","age":"29","a":[1,2],"b":("12",2)}
# print(a["name"])
# a["weight"] = 100
# print(a)
# a["age"] = "26"
# print(a)

# b = a.get("name")
# print(b)
# b = a.pop("a")
# print(b)
# print(a)
# a.update(name = "李四")
# print(a)


'''
print(a.get("name"))
print(a["name"])
print(a)
del a["a"]
print(a)

m = [1,2,3,4,5,"12","nihao","你好","你好"]
print(m)
del m[-1]
print(m)
'''


name = input("请输入姓名：")
age = input("请输入年龄：")
sex = input("请输入性别：")
# a = {"name":name,"age":age,"sex":sex}
userinfo = {}
userinfo.update(name = name,age = age, sex = sex)
print(userinfo)
