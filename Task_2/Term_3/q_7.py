# 7. Write a Program to accept a two number and find sum of Two even No.

# num1 = int(input('Enter the first numebr :'))
# if(num1 % 2 == 0):
#     print('The given no is valid')
# else:
#     print('Plz enter valid even no:')

# num2 = int(input('Enter the second numebr :'))
# if (num2 % 2 == 0):
#     print('The given n is valid')
# else:
#     print('Plz enter valid even no:')

# sum = num1 + num1
# print('The sum of even nos',sum)


while True:
    num1 = int(input('Enter the first even number: '))
    if num1 % 2 == 0:
        break  
    print('Error: That is an odd number. Try again!')

while True:
    num2 = int(input('Enter the second even number: '))
    if num2 % 2 == 0:
        break 
    print('Error: That is an odd number. Try again!')

total = num1 + num2
print('The sum of the two even numbers is:', total)
