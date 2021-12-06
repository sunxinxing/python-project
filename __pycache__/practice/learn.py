def isequal(x,y):
    if (x<y):
        print('too small')
        return False;
    if (x>y):
        print('too big')
        return False;
    if(x==y):
        print('bingo')
        return True
    return
#print('请输入x：')
#num1=input()
#print('请输入y：')
#num2=input()
#isequal(num1,num2)
from random import randint
num = randint(1,100)
print('guess what i think：')
bingo = False
while bingo == False:
    answer = int(input())
    bingo = isequal(answer,num)
