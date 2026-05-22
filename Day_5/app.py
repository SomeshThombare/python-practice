#when we run the or import a module it is excute only once by pyton virtual machine by line.
# module object is cretted adn a seperate mamespace is create for each module attached with the module object.
#module object is cached is sys.module.
#for execution of modulw stack is created and push it on call stack.
#so module - module srack frame is created only once.
#once module executon complete stack frame is destoryed.

import sys
import os

print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)

# print(sys.path)
print('File Path: ',__file__)
print('Module Name: ',__name__)
print('process ID', os.getpid())
# print(sys.modules)

#find the .py executale file
print(sys.executable)

# resue module by interpreter,will get module object
print(sys.modules['__main__'])

#how to check the preloaded moduel and there counts
print('toal moduel loaded', len(sys.modules))





