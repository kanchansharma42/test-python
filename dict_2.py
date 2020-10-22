#dictionary
from dict import stu_detail
'''keys_name = ['name','marks','subjects']
keys_val = ['ram',22,'eng']
my_list = zip(keys_name,keys_val)
print(my_list)
my_dict = dict(my_list)
print(my_dict)'''

my_dict = {'name': 'ram', 'marks': 25, 'subjects': 'eng'}
my_class = {'student1': {'name': 'shyam', 'marks':23,'subjects': 'math'},
'student2': {'name': 'sham', 'marks': 23,'subjects': 'math'},
'student3': {'name': 'shya', 'marks': 23,'subjects': 'math'},
'student4': {'name': 'shyama', 'marks': 23,'subjects': 'math'},
'student5': {'name': 'shyamal', 'marks': 23, 'subjects': 'math'}}

print(my_class['student1']['name'])
print(my_class['student1']['name'])
ask = input("Are you a student or teacher  ")

if ask == 'teacher':

    k = len(my_class) + 1
    con = input('Do you want to add.enter y or n')
    while con == 'y':
        n = input('enter name')
        m = input('enter marks')
        s = input('enter sub')
        my_class['student' + str(k)] = {'name': n, 'marks': m, 'subjects': s}
        k = k+1
        con = input('Do you want to add.enter y or n  ')
    print(my_class)
    for i in my_class:
        name = my_class[i]['name']
        marks = my_class[i]['marks']
        subjects = my_class[i]['subjects']
        stu_detail(name, marks, subjects)
elif ask == 'student':
    stuname = input('enter your name  ')
    stu_list=[]
    for i in my_class:
        stu_list.append(my_class[i]['name'])
        if stuname == my_class[i]['name']:
            stu_marks = my_class[i]['marks']
            stu_sub = my_class[i]['subjects']
            print(f' {stuname} your marks are {stu_marks} and You have {stu_sub}')
            break
else:
    print('not valid entry')





