class A:
    def m1(self):
        print('Class A m1() method calling....')
class B(A):
    pass

b = B()
b.m1()