f = open('C:\\Users\\User\\Documents\\test.txt')
data = f.read()
print(data)

f = open('C:\\Users\\User\\Documents\\output.txt','w')
out = f.write(data)

f.close()

print('请输入：')
i = input()
f = open('C:\\Users\\User\\Documents\\output22212.txt','w')
out = f.write(i)
f.close()
