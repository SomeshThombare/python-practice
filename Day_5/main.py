# print('This is main.py file')
# import second # 
# import second #reuse the 
# import second #

# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# # print(dir(second)) # show module object structure
# # print('_________________________________________________________________________')
# # print(second.__dict__) # show module object strucure, priting namespace of module.

import sys 
import second

def by():
    pass
class Emp:
    pass

# print('second.py module namespace', globals().keys() )
# print('------------------------------------------------')
# print('main.py module namespace',second.__dict__.keys())
# print('End of second .py file execution')


# print(fourth.a)

# print(sys.modules['second'.__dict__['a']])

'''
#local and global variabes in stack fraem
a = 100
def m1():
    a = 10000
    frame = sys._getframe() # get functon stack frame
    print('Fuction frame locals:',frame.f_locals)
m1()


frame = sys._getframe()
# print("Module frame locals/gloabals",frame.f_locals)
print('-----------------------------------------------------')
print("Module frame locals/gloabals",frame.f_globals)

'''

"""
import inspect

def a():
    b()

def b():
    c()

def c():
    d()

def d():
    for frame in inspect.stack():
        print(frame.function)

a() #stack frames are created and push on call stack or stack memory.

"""

# buitinies modules
import builtins
import sys
print(id (builtins.print))# it is moduel loded at the time of interpreter start
print(id(__builtins__.__dict__['print']))

print(id(sys.modules['builtins'].__dict__['print']))

#reseu the buitltins and module 
print(id(builtins))
print(id(sys.modules['builtins']))


