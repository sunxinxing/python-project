f = open('C:\\Users\\User\\Documents\\test.txt')
data = f.read()
print(data)
f.close()

f = open('C:\\Users\\User\\Documents\\test.txt')
data = f.readline(2)
print(data)
f.close()

f = open('C:\\Users\\User\\Documents\\test.txt')
data = f.readlines()
print(data)
f.close()


f = open('C:\\Users\\User\\Documents\\test.txt','a')
data = f.write('"\n我是新加的。"')
print(data)
f.close()
