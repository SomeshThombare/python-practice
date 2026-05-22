# 11. Write a Program to create Menu driven program for Arithmetic Operation
n = int(input('Enetr operation numer 1 = Add , 2 = sub , 3 = mul, 4 = div, 5 = mod :'))

num1 = int(input('Enter the first numebr :'))
num2 = int(input('Enter the second numebr :'))


if ( n == 1):
    print('Additon :',num1 + num2)
elif(n == 2):
    print('Substraction : ',num1 - num2)
elif(n == 2):
    print('Multiplcation :',num1 * num2)
elif(n == 2):
    print('Division :',num1 / num2)
elif(n == 2):
    print('Mod :',num1 % num2)