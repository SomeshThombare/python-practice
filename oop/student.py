class Student:
    def __init__(self, Name, Marks, Roll_no):
        self.name = Name
        self.marks = Marks
        self.roll_no = Roll_no

    def stud_detail(self):
        print(f"{self.name} {self.marks} {self.roll_no}")

s1 = Student('Sam', 90, 64)
s1.stud_detail()
