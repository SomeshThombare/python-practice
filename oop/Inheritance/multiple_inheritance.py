class A:
    def m1(self):
        print('class A')

class B:
    def m2(self):
        print('Class B m2() method')

class C(A,B):
    def m3(self):
        print('Class C under m3() method calling.')

c = C()
c.m3()
c.m1()
c.m2()



