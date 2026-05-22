class Student:
    college_name = 'Skille IT Academy' #here college_namee is a class/static varible
    
    def __init__(self, name, marks, roll_no):
        """student class constructor"""
        self.name = name
        self.marks = marks
        self.roll_no = roll_no

s1 = Student('sam', 20, 24)
s2 = Student('somnath', 55, 21)
s3 = Student('Somesh', 33, 21)

print('class_name_space :', Student.__dict__)

print('\n')
print('Object_s1_namespace',s1.__dict__)


print('\n')
print('Object_s2_namespace',s2.__dict__)


print('\n')
print('Object_s3_namespace',s3.__dict__)

print('-------------------------Access the static variable------------------------------------')
print(Student.college_name) # accessign of satic varible
print(s1.college_name) 
print(s2.college_name)
print(s3.college_name)