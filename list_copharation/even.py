# even_numbers = []
# for x in range(21):
#     if x % 2 == 0:
#         even_numbers.append(x)
# print(even_numbers)


# list cophration

# my_even_nums = [ append | for loop  | condition   ] # if conditon is true then only appen into list

my_even_nums = [x for x in range(21) if x % 2 == 0]
print(my_even_nums)  

# #usign ternery operator
# my_even_nums = ['even ' x % 2 == 0 else 'odd' x for in range(21)]
# print(my_even_nums)
print('\n')



# print the squre roots
print('-------------------------SQRT----------------------------------------------')
sqrt = [x*x for x in range(21)]
print(sqrt)

print('\n')



print('-------------------------Tuple Copphersion------------------------')
# tupel cophersion
print('---Even odd nums-----')
even_nums = tuple( 'even' if x % 2 == 0 else 'odd' for x in range(0,21))
print(even_nums)
print('\n')



print('----SQRT nums----(0,21-------)')
sqrt_tupel = tuple(x*x for x in range(21))
print(sqrt_tupel)

print('\n')

# find the ecn nums in given in my_list then stor those numsin new_mY_list
print('--------------Probelm NO 1----------------------')
my_list = [x for x in range(0,11)]
my_new_list = [ x for x in my_list if x % 2 == 0]
print('My lIst :',my_list)
print('Sort the even nums from my_list : ',my_new_list)

print('------------------DICT Copherion--------------------------------------------------------')
even_nums = {x: 'even' if x % 2 == 0 else 'odd' for x in range(0,21)}
print(even_nums)
print('\n')


print('----------------------------------------------------------------------------------------------------------------')

db = {x : x*x for x in range(11)}

def  get_student(id):
    if id in db:
        return "id is already present"
    db[id] = id + id
    return db

my_dict  = get_student(1)
print(my_dict)
my_dict = get_student(14)
print(my_dict)

