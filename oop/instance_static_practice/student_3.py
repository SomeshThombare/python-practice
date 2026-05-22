
student_db = {}
class Student:
    college_name = 'SIT'

    def __init__(self, name, marks, roll_no):
        self.name = name
        self.marks = marks
        self.roll_no = roll_no

    def print_stud_detail(self):
        print(f"Student Name: ", self.name)
        print(f"Studetn marks: ",self.marks)
        print(f"Student Roll Number :", self.roll_no)
        print('-------------------------------------------------------------------')

s1 = Student('sam', 20, 24)
s1.print_stud_detail()
s2 = Student('somnath', 55, 21)
s2.print_stud_detail()
s3 = Student('Somesh', 33, 21)
s3.print_stud_detail()

print('-----------------------------------------------------------------------')
print('using for loop on dict')

student_db[s1.roll_no] = s1
student_db[s2.roll_no] = s2
student_db[s2.roll_no] = s3

# print(student_db)

for Student in student_db.values():
    Student.print_stud_detail()