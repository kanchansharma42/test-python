#to check upper case and lower case letters in a string
#to display upper and lower case letters too

#input_str = input('enter a string  ')

upper_let = 0
lower_let = 0
upper_list = []
lower_list = []

'''for i in input_str:
    if i.isupper():
        upper_let = upper_let + 1
        upper_list.append(i)
    else:
        lower_let = lower_let + 1
        lower_list.append(i)
#print(','.join(upper_list))
#print('No of Upper case letter are  ' + str(upper_let) +  ' upper case letters are   ' + ','.join(upper_list))'''

stu_name = ['ram', 'shyam', 'raj','reena']
stu_age = [22, 33, 44, 12]
a = 0
for i in stu_name:
    #age = stu_age.pop()
    age = stu_age[a]
    print(f'hello {i} your age is {age}')
    a = a + 1


#print('my name is {} and my age is {} '.format('kanchan',2) )
