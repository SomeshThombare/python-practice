# clourees:
# Function remembers value even after outer functio is gone.
# Even after fun1() finished, fun2() rememberes name variable value.

def fun1(name):
    def fun2():
        print(f" hello {name}")
    return fun2

my_var = fun1('Sam')
my_var()



print('----------------------------------------')

def outer():
    # x = 100
    def inner():
        print('This is iner function ')
    return inner

