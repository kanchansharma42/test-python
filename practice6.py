#FUNCTIONS

def kanchan_add (a,b):
    print(a +  b)

    #print(c)

def kanchan_sub (a,b):
    print(a - b)

def kanchan_multi(a,b):
    print(a * b)

def kanchan_div(a,b):
    print(a / b)

def kanchan_pop(*args):
    for i in range(len(args)):
        a = -1 - i
        # kanchan_pop()
        # pop_list = stu_name.pop()
        print(args[a] + '  is out')

def odd_even(num):
    if num%2 == 0:
        print('num is even')
    else:
        print('num is odd')





