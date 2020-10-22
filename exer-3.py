
#class_dict = {'stu1': {'name' : 'rani', 'age' : 10, 'class' : 3},
              # 'stu2' : {'name' : 'tani', 'age' : 12, 'class' : 5},
              # 'stu3' : {'name' : 'bani', 'age' : 13, 'class' : 6}}
stu_dict={}
#taking data from teacher
def teacher():
    stu_info_keys = ['name','age','class']
    class_dict_keys = ['stu1','stu2','stu3']
    class_dict_values = []
    for i in range(3):
         stu_info_values = []
         name = input('Enter student name ')
         age = input('enter student age ')
         sclass = input('enter student class ')
         stu_info_values.append(name)
         stu_info_values.append(age)
         stu_info_values.append(sclass)
         stu_detail = zip(stu_info_keys, stu_info_values)
         stu_dict = dict(stu_detail)
         class_dict_values.append(stu_dict)
    class_dict_zip = zip(class_dict_keys, class_dict_values)
    class_dict = dict(class_dict_zip)
    print(class_dict)

def student():

    stuname = input('Enter your name ')
    for i in class_dict:
        if stuname == class_dict[i]['name']:
            stu_cls = class_dict[i]['class']
            stu_ag = class_dict[i]['age']
            print(f'{stuname} your class is {stu_cls} and your age is {stu_ag}')
        #else:
        #   print('name not in list')

que = input('Are you student or teacher ')
if que == 'teacher':
    teacher()
elif que == 'student':
    student()
else:
    print('Invalid Entry')