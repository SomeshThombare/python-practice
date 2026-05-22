class A:
    def m1(self):
        print('A class method m1() caling.........')
        
class B(A):
    def m2(self):
        print('B class method m2() caling.........')

class C(B):
    def m3(self):
        print('C class method m3() caling.........')
        
class D(B):
    def m5(self):
        print('D class  caling.........')

class E(C,D):
    def m5(self):
        super().m5()
        print('E class m5() method....calling')


e = E()
e.m1()
e.m5()