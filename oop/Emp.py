class Emp:
    def __init__(self, Name, Age, Salary):
        self.name = Name
        self.age = Age
        self.sal = Salary

    def emp_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Salaey: {self.sal}")

#usind methods
e1 = Emp('Sam', 21, 50000)
e1.emp_details()

#2 nd way to print the details
e2 = Emp('Somnath', 22, 80000)
print(e2.__dict__)

        