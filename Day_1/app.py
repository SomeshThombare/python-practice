# global namespace == moudule / python file run kartha teva global namespace create hoto.

a = 10
b = 20
b = a 
c = a + b
print(c)
print(type(a))
print('a',id(a))
print('b',id(b))


def show():
	d = 100 # local variable = local namwspace == menas stack frames 
	  #when we call a function
print('local namespaces',locals())

class A:
	#local namespace
	def sayHello(self):
		e = 1000

show()

print('global namespaces',globals())