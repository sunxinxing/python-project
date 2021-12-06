from string import *
f = open('C:\\Users\\User\\Documents\\scoretest.txt')
lines = f.readline()
#print(lines)
f.close()

result = []
for line in lines:
   # print(line)
    data = line.split()
   # print(data)

    sum = 0
    for score in data[1:]:
     sum += int(score)
    result = '%s \t: %d\n' % (data[0],sum)
    results = result.append(result)

output = open('C:\\Users\\User\\Documents\\test11.txt','w')
output.writelines(results)
output.close()
