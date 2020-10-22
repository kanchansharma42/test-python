#class
a = 'hello'
print (type(a))

class student:
    def __init__(self,first,last):
        self.firstname = first
        self.lastname = last
    def mail(self):
        print(f'{self.firstname}.{self.lastname}@gmail.com')

student1 = student('ram','sharma')
print (type(student1))
student2 = student('ravan','verma')

print(student1.firstname)
print(student2.lastname)
student2.mail()