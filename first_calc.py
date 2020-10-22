from practice6 import kanchan_add
from practice6 import kanchan_sub
from practice6 import kanchan_multi
from practice6 import kanchan_div

print('Operation Choices:\n'
      'A. Press 1 for Addition \n'
      'B. Press 2 for Subtraction \n'
      'C. Press 3 for Multiplication\n'
      'D. Press 4 for Division\n')

operator = input(' Enter your Choice :  ')
d = int(input('enter num1 '))
e = int(input('enter num2 '))

if operator == '1':
    kanchan_add(d,e)

elif operator == '2':
    kanchan_sub(d, e)

elif operator == '3':
    kanchan_multi(d, e)

elif operator == '4':
    kanchan_div(d, e)

else:
    print('Wrong Choice')





