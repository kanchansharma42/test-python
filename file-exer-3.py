
#class_dict = {'stu1': {'name' : 'rani', 'age' : 10, 'class' : 3},
              # 'stu2' : {'name' : 'tani', 'age' : 12, 'class' : 5},
              # 'stu3' : {'name' : 'bani', 'age' : 13, 'class' : 6}}
stu_dict={}
#taking data from teacher

def teacher():
    tchr_work = input('Do you want to read or add record ')
    if tchr_work == 'read':
        with open('C:\\Users\\HP\\Desktop\\test.csv', 'r') as f:
            for i in f:
                print(i)

    elif tchr_work == 'add':
        #data = " "
        stu_info_values = []
        name = input('Enter student name ')
        age = input('enter student age ')
        sclass = input('enter student class ')
        stu_info_values.append(name)
        stu_info_values.append(age)
        stu_info_values.append(sclass + '\n')
        #final_rec = ','.join(stu_info_values)
        #print(final_rec)

        with open('C:\\Users\\HP\\Desktop\\test.csv','r+') as f:
            tot_rec = len(f.readlines())
            print(f'there are {tot_rec} records in list')
            f.write(','.join(stu_info_values))
            print('Added Record')
            #data == f.read()
            f.seek(0)
            tot_rec = len(f.readlines())
            print(f'Now there are { tot_rec} records in list')
            for i in f:
                print(i)
    else:
        print('wrong entry')

def student():

    stuname = input('Enter your name ')
    with open('C:\\Users\\HP\\Desktop\\test.csv','r') as f:
        for i in f:

            list_line = i.split(',')
            #print(list_line)

            if stuname == list_line[0]:
                stu_cls = list_line[1]
                stu_ag = list_line[2]
                print(f'{stuname} your class is {stu_cls} and your age is {stu_ag}')
                break


        #else:
         #  line = f.readline()

que = input('Are you student or teacher ')
if que == 'teacher':
    teacher()
elif que == 'student':
    student()
else:
    print('Invalid Entry')