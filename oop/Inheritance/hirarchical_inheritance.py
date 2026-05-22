class A:
    def a(self):
        print('This is Classs A with a() Meethod')

class B(A):
    def m1(self):
        print('This is class B with m1() class')

class C(A):
    def display(self):
        print('this is calss c with display method...')

c = C()
c.display()
c.a()
b = B()
b.m1()
b.a()
