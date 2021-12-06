

list = [1, 2, 3]

#append--列表末尾
list.append("姓名")
print(list)

#insert(下标，值)

list.insert(1,"name")
print(list)

#extend--序列
list1 = ["A", "B", "C"]
list_new = ["时间", "地点"]
list1.extend(list_new)
list_new.extend(list1)
print(list1)
print(list_new)

list2 = [1, 3, 5, 7, 9, 3]

#remove---移动
list2.remove(3)
print(list2)

#pop--默认下标为-1，删除末尾，该方法有返回值
print(list2.pop())
print(list2)

#clear--清空
# list2.clear()
# print(list2)

#del/pop，若取出值后还需要使用，则用pop；否则用del

#del--删除指定值
del list2[1]
print(list2)


#reverse --排序
list3 = ["一班", "二班", "三班", "四班", "五班", "三班"]
list3.reverse()
print(list3)

#index--获取下标
print(list3.index("三班"))

#count--某元素的个数
print(list3.count("一班"))

#修改元素
list4 = [1, 3, 4]
list4[2] = "name"
print(list4)



