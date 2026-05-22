emp_db = {}
class Employee:
    def __init__(self,name, age, salary):
        self.name = name
        self.age = age
        self.sal = salary

    def print_emp_detail(self):
        print(f'Employee Name :',{self.name})
        print(f"Employee Age :", {self.age})
        print(f"Employee Salary : ",{self.sal})
        print('-------------------------------------------------')

e1 = Employee('sam', 21, 90000)
e2 = Employee('somnath', 22, 80000)
e3 = Employee('Somesh ', 33, 50000)


emp_db[e1] = e1
emp_db[e2] = e2
emp_db[e3] = e3



for Employee in emp_db.values():
    Employee.print_emp_detail()