class Student:
    college_name = 'SIT'
    def __init__(self, name, marks, roll_no):
        self.name = name
        self.marks = marks
        self.roll_no = roll_no
        Student.x = 10

    def m1(self):
        print(self.name, self.marks, self.roll_no)

print('Using method callin.............')
s1 = Student('sam', 20, 24)
s2 = Student('somnath', 55, 21)
s3 = Student('Somesh', 33, 21)

s1.m1()
s2.m1()
s3.m1()

print('-------------------------------------------------')

#accesig of instance variable outside of classs body
print('using instace variable.........')
print(s1.name, s1.marks, s1.roll_no)
