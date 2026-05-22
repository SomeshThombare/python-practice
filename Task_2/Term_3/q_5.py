# 5. Write a Program to accept two number and find smallest no.
num1 = int(input('Enter the first numebr :'))
num2 = int(input('Enter the second numebr :'))

if(num1 < num2):
    print(num1,'is smallest No')
elif(num2 < num1):
    print(num2,'is smallest no')
else:
    print('Enter the valid no')