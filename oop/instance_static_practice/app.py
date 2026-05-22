import sys

class A:
    def m1():
        a = 10

    def m2():
        b = 20

c = 40


a1 = A()
a2 = A()
a3 = A()
    
print(sys.modules)
print('-------------------------------------')
print(globals())
print('\n')

print(a1.__dict__)
