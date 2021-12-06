
'''
for i in range(1,9,3):
    print(i)

for i in range(1,9):
    print(i)

for i in range(5):
    print(i)

list = list(range(1,8))
print(list)


str = 'python'
for i in range(0,len(str)):
    print(str[i])

'''
#continue--跳出当次循环
for i in 'python':
    if i == 't':
        continue
    print(i)

#break--跳出整个循环
for i in 'python':
    if i == 't':
        break
    print(i)