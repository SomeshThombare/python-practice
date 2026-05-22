class A:
    x = 10 # static/class variabel, classnamespace

    def __int__(self):
        self.y = 20 # here self.x is instance variable, instance object namespace
print('Class_name_space :', A.__dict__)

a1 = A()
a2 = A()

print('\n')
print('object_a1_name_space',a1.__dict__)

print('\n')
print('object_a2_name_space',a2.__dict__)


