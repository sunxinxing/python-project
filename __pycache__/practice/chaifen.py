from random import choice

score = [0,0]
direction = ['left','center','right']

def kick():
  print('===You Kick!===')
  print('choose one side to shoot: left,center,right')
  #print('left,center,right')
  you = input()
  print('you kicked '+ you)
  com = choice(direction)
  print('computer saved '+ com)
  if (you != com):
    print('goal!')
    score[0] += 1
  else:
    print('opps...')

  print('score: %d(you) : %d(com)\n'%(score[0],score[1]))

  print('===You Save===')
  print('choose one side to save: left,center,right')
  you = input()
  print('you saved:' + you)
  com = choice(direction)
  print('com kicked:' + com)
  if(you == com):
      print('saved!')
  else:
      print('opps...')
      score[1] += 1
  print('score : %d(you) : %d(com)\n'%(score[0],score[1]))

for i in range(5):
    print('===Round %d==='%(i+1))
    kick()

while(score[0] == score[1]):
    i += 1
    print('===Round==='%(i + 1))
    kick()
if(score[0] > score[1]):
    print('you win!')
else:
    print('you lose...')
#kick()
