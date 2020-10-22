name_of_students = ['ram', 'shyan', 'rohan']
print(name_of_students)
print(type(name_of_students))

highest_marks = (100, 100, 200)
print(highest_marks)
print(type(highest_marks))

roll_no = {}
print(type(roll_no))

marks = set(highest_marks)
print(type(marks))
print(marks)

name = input('enter your name : ')

if name.lower() == 'ram' or name == 'madhav':
    print('go to computer science')
elif name.lower() == 'shyan':
    print('go to snaskrit')
else:
    print('go to physical education')

if name.islower():
    print('A')



