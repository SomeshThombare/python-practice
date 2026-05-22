class A:
    """-------------------instance varible...--------------------------"""
    def __init__(self, first, second):
        self.first_num = first
        self.second_num = second

    def add_to_num(self):
        print(f"{self.first_num} + {self.second_num} = {self.first_num + self.second_num}")

obj = A(45,18)
obj.add_to_num()


print('------------------------------Using static variable--------------------------')
class B:
  #addition of two static variable
    first_num = 10
    second_num = 30

    def add_to_num(self):
        print(f"{self.first_num} + {self.second_num} = {self.first_num + self.second_num}")

obj = B()
obj.add_to_num()

print('--------------------@Classmethod-------------------------------------')

class C:
  #addition of two static variable
  
    first_num = 100
    second_num = 300
    @classmethod
    def add_to_num(self):
        print(f"{self.first_num} + {self.second_num} = {self.first_num + self.second_num}")

C.add_to_num()

print('-------------------------all of them -----------------------')

class D:
    a = 1000
    b = 2000

    def __init__(self,x,y):
        """--------constructor use to define instance variable----------"""
        self.x = x
        self.y = y

    def display_addition(self):
        """Instacce method proess object informaion  or instance variable """
        print(f"{self.x} + {self.y} = {self.x + self.y}")

    @classmethod
    def add_to_nums(cls):
        '''class method process bthe object information or static variable'''
        print(f"{cls.a} + {cls.b} = {cls.a + cls.b}")

    @staticmethod
    def result(a,b):
        """static meethod procces local varible"""
        """here a and b are the parameter varibale which alos local variable"""
        print(f'{a} + {b} = {a + b}')

obj1 = D(100,200)
obj1.display_addition()
# obj1.display_addition()

obj2 = D(50,200)
obj2.display_addition()

D.add_to_nums()
D.add_to_nums()


print('---------------class method thorugh addtion of two num------------------------')

D.result(5,5)