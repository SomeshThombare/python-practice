#higher order function  / first class function
'''1st point'''
def  say_hii():
    print('hey_hii')

say_hii()
#we assign fun object to the varible usign = operator
my_var = say_hii
my_var()
print('--------------------------')


'''2nd  point '''
def fun1(my_var):
    print('I am function 1')
    # This calls the function you passed in
    my_var() 

def fun2():
    print('I am function 2')

# Pass fun2 into fun1
# my_var() 
fun1(fun2)


print('-------------------------------------------------------------------')


''' 3rd point '''
#Here fun 2 is nested  function
def fun1():
    def fun2():
        print('i am function2')
    return fun2
#fun1 return fun2 ibject and using = operator we will asssign it into my_var varible.
my_var = fun1()
my_var()

print('-------------------------------------------------------------------')


'''4th point '''
#assign function to the varible
def  fun1():
    print('I an funtioin 1')

#assign function to the varibke
my_var = fun1

print(id(my_var),id(fun1))
print(type(my_var),type(fun1))
print(my_var,fun1)

fun1()
my_var()

print('-------------------------------------')

