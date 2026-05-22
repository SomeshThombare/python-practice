#write a programm to print 2's table
r  = range(2, 21,2)
# print(r)
for i in r:
    print(i)

print('---------take userr from input--------------')
table = int(input('Enter the table number:'))
for num in range(1,11):
    print(num * table)
    