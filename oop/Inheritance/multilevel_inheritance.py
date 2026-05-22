class A:
    def m1(self):
        print('Class A m1() method calling....')
class B(A):
    def m2(self):
        print('This is class B with m2()method...')

class C(B):
    pass

c = C()
c.m1()
c.m2()