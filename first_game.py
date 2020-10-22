print('Games Choices\n'
      'A. Press 1 for Rock\n'
      'B. Press 2 for Stone\n'
      'C. Press 3 for Paper\n'
      'D. Press 4 for Scissor\n')
'''t1 = 0
t2 = 0'''

i=0
values = ['1','2','3','4']
while (i < 3):
    t1 = input(' Enter Player1 choice ')
    t2 = input(' Enter Player2 choice ')
    if t1 in values and t2 in values:
        if t1 == t2:
            print('Tie')
        elif t1 == '1':
            print('Player 1 is winner')
            print('Game Over')
            break
        elif t2 == '1':
            print('Player 2 is winner')
            print('Game Over')
            break
        elif t1 == '2' and t2 == '3':
            print('Player 2 is winner')
            print('Game Over')
            break
        elif t1 == '2' and t2 == '4':
            print('Player 1 is winner')
            print('Game Over')
            break
        elif t1 == '3' and t2 == '4':
            print('Player 2 is winner')
            print('Game Over')
            break
    else:
        if i == 2:
            print('Game Over')
        else:
            print('Enter again')
    i = i + 1
print('test')
