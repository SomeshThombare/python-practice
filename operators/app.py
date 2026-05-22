print(10 + 20)
print('10' + '10')
print(3 * 'A')
print(2 * ('A' + 'a'))

print(10/2)
print(10%2)

print('Divison is return question (13/3):',13/3)
print('Modules operator retur Reminder(13%3) :',13%3)

#relatonal / conditional operator
a = 10
b = 20

# > --> greater than
#   < --> less than
#   >= --> greater than equal to
#   <= --> less than equal to
#   == --> equal to - equal to 
#   != --> not qual to

print(a > b) # false
print(a < b) # true

# Logical operator
a = 10
b = 20
# and , or , and
print(a > b and a < b)
print(a > b or a < b)

# assignmetn operator

''' =:
 to assign / store/ modify/ re-assign RHS address to LHS variable

           <------------------------
               2              1
               LSH           RHS
               varibale obect creation / metod caling
                                    
pyton supper special type of assignment
    +=, -+, /=, *=, %=

'''

a = 10
print(a)

a += 2 
print(a)

a -= 2
print(a)

a *= 2
print(a)

a /= 2
print(a)

# ternory operator
print('first_value' if a < b else 'second_value' )

