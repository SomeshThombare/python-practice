# 8. Write a Program to accept a two number and find sum of Two odd No.
while True:
    num1 = int(input('Entet the first odd no: '))
    if(num1 % 2 != 0):
        break
    print('Error: this is not odd number, Try again!')

while True:
    num2 = int(input('Enter the second odd number: '))
    if(num2 % 2 != 0):
        break
    print('Error: this is not a odd no, Try again!')
sum = num1 + num2
print('the sum of of two add numbers: ',sum)