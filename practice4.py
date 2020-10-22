''' 1) range

3) While
4) Basic Functions
5) Dictionary'''



student = {'first_name':'madhav','second_name':'sharma','roll_no':10}
student1 = {'first_name':'mad','second_name':'shrma','roll_no':11}
# print(len(student.keys()))
# print(len(student.values()))
# print(student.items())
# print(len(student['first_name']))
#print(list(student['first_name'])[0])
name = student['first_name']
abc = list(name)
a = abc[0]
#print(a)
#print(student1['first_name'])

received = {
  "version": 4,
  "terraform_version": "0.12.29",
  "serial": 0,
  "lineage": "5550f82d14c5419"}
#print('the s/w version is ' + str(received['version']))


newlist=[3,2,5]
#print(newlist[-1])

i = 0

while (i<len(abc)) :
    #print(i)

    if(abc[i] == 'a'):
        print('E')
    else:
        print(abc[i])
    i = i+1
