# 6. Write a Program to accept two number and find find largest no.

num1 = int(input('Enter the first numebr :'))
num2 = int(input('Enter the second numebr :'))

if(num1 > num2):
    print(num1,'is largest No')
elif(num2 > num1):
    print(num2,'is largest no')
else:
    print('Enter the valid no')