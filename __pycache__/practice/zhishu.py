num = int(input('输入一个任意的大于1的整数：'))

i = 2
flag = True
while i < num:
    if num % i == 0:
        flag = False
    i += 1

if flag:
    print(num,'是质数')
else:
    print(num,'不是质数')