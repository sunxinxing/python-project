
'''
age = int(input("输入年龄："))

if age >= 60:
    print("免票")
elif age >=12 and age <= 59:
    print("成人票")
elif age >= 4 and age <= 11:
    print("儿童票")
elif age >0 and age <=3:
    print("婴儿免票")

'''


'''
height = float(input("身高："))
money = float(input("收入（万）："))


if height >= 178:
    if money >= 100:
        print("高富帅")
    else:
        print("高但没钱")
else:
    print("再见")

'''

for i in "12":
    print("hello")

for j in [1, 2]:
    print("hi")

dict = {"ele1" : [1, 2], 
        "ele2" : "你好", 
        "ele3" : 1, 
        "ele4" : 1.0, 
        "ele5" : {"A", "B", "C"}}

for key in dict.keys():
    print(key)

for value in dict.values():
    print(value)

for key, value in dict.items():
    print(key, value)

