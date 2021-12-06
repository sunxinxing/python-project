from time import *
start = time()
i = 2
while i <= 10000:
    flag = True
    j = 2
    # while j < i:
    while j <= i * 0.5:
        if i % j == 0:
         flag = False
         break
        j += 1
    # if flag:
    #      print(i)   
    if flag:
         pass
    i += 1
    
finish = time()
# time = finish - start
print(finish - start,"秒")
