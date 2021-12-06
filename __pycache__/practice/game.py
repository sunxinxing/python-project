name1 = '唐僧'
name2 = '白骨精'

#print('-'*20,'欢迎光临《唐僧大战白骨精》','-'*20)
print('-'*20,f'欢迎光临《{name1}大战{name2}》','-'*20)

# print('请选择你的身份：')
# print('\t1.唐僧')
# print('\t2.白骨精')

# player_choose = input('请选择[1-2]：')

# print('-'*66)

# if player_choose == '1':
#     print('你已经选择了1，你将以唐僧的身份来进行游戏！')
# elif player_choose == '2':
#     print('你竟然选择了白骨精，太不要脸了，你将以白骨精的身份来进行游戏！')
# else:
#     print('你的输入有误，系统将自动分配身份，你将以唐僧的身份进行游戏！')

# player_life = 2 #生命值
# player_attack = 2 #攻击力

# boss_life = 10
# boss_attack = 10

# print('-'*66)
# print(f'唐僧，你的生命值是{player_life}，攻击力是{player_attack}')


# while True:
#     print('-'*66)
#     print('请选择你要进行的操作：')
#     print('\t1.练级')
#     print('\t2.打boss')
#     print('\t3.逃跑')
#     game_choose = input('请选择要做的操作[1-3]：')

#     if game_choose == '1':
#         player_life += 2
#         player_attack += 2
#         print('-'*66)
#         print(f'唐僧恭喜你升级了，现在你的生命值是{player_life}，攻击力是{player_attack}')
#     elif game_choose == '2':
#         boss_life -= player_attack
#         print('-'*66)
#         print('唐僧攻击了白骨精')
#         if boss_life <= 0:
#             print(f'白骨精受到了{player_attack}点伤害，唐僧胜利！')
#             break
#         player_life -= boss_attack
#         print('白骨精攻击了唐僧')
#         if player_life <= 0:
#             print(f'唐僧受到了{boss_attack}点伤害，game over！')
#             break
#     elif game_choose == '3':
#         print('-'*66)
#         print('唐僧跑了，game over！')
#     else:
#         print('-'*66)
#         print('你的输入有误，请重新输入！')




print('请选择你的身份：')
print('\t1.唐僧')
print('\t2.白骨精')

player_choose = input('请选择[1-2]：')

print('-'*66)

if player_choose == '1':
    print('你已经选择了1，你将以唐僧的身份来进行游戏！')
elif player_choose == '2':
    print('你竟然选择了白骨精，太不要脸了，你将以白骨精的身份来进行游戏！')
else:
    print('你的输入有误，系统将自动分配身份，你将以唐僧的身份进行游戏！')

player_life = 2 #生命值
player_attack = 2 #攻击力

boss_life = 10
boss_attack = 10

print('-'*66)
print(f'唐僧，你的生命值是{player_life}，攻击力是{player_attack}')


while True:
    print('-'*66)
    print('请选择你要进行的操作：')
    print('\t1.练级')
    print('\t2.打boss')
    print('\t3.逃跑')
    game_choose = input('请选择要做的操作[1-3]：')

    if game_choose == '1':
        player_life += 2
        player_attack += 2
        print('-'*66)
        print(f'唐僧恭喜你升级了，现在你的生命值是{player_life}，攻击力是{player_attack}')
    elif game_choose == '2':
        boss_life -= player_attack
        print('-'*66)
        print('唐僧攻击了白骨精')
        if boss_life <= 0:
            print(f'白骨精受到了{player_attack}点伤害，唐僧胜利！')
            break
        player_life -= boss_attack
        print('白骨精攻击了唐僧')
        if player_life <= 0:
            print(f'唐僧受到了{boss_attack}点伤害，game over！')
            break
    elif game_choose == '3':
        print('-'*66)
        print('唐僧跑了，game over！')
    else:
        print('-'*66)
        print('你的输入有误，请重新输入！')
        