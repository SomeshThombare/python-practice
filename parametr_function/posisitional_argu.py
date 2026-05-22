# posisitional argument
def print_details(name, age):
    print(f'my name is {name}')
    print(f'my age is {age}')

print_details('sam',21)

print_details('21','SAM') # my name is 21 and age  is sam 

print_details(21,'sam') # my name is 21
                        #  my age is sam

print_details('sam') #TypeError: print_details() missing 1 required positional argument: 'age'
