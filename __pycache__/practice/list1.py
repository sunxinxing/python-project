from random import choice
print("请输入方向：")
print('"左"、"中"、"右"')

local = input()
print("'you kicked'+local")
direction = ['左','中','右']
com = choice(direction)
print('电脑输出为：'+com)

if(local != com):
    print('得分！')
else:
    print('oops...')
