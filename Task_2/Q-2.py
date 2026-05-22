# 1) Generate the Series... 2 4 6 8 10 12 14 16 18 20.
for i in range(2,21,2):
    print(i)

print('--------( 9 table)------')
# 2) Generate the Series... 9 18 27 36 45 54 63 72... 90
for i in range(9,91,9):
    print(i)

print('-------------(1 -2 3 -4...)-------------------------')
# 3) Generate the Series... 1 -2 3 -4 5 -6 7 -8 9 -10 
for i in range(1,11):
    if i % 2 == 0:
        print(-i, end=' ')
    else:
        print(i, end=' ')
print('\n')

print( '-------(5 table )---------------------------------')
# 4) Generate the Series... 5 10 15....50
for i in range(5,51,5):
    print(i)

print('----------------(1,10,100,1000.....)----------------')
# 5) Generate the Series... 1 10 100 1000.
for i in range(4):
    print(10 ** i, end=' ')

print('-----------(i+j)---------')
# 6) Generate the Series... 1 3 6 10 15 21 28 36 45.
j = 0
for i in range(1,11):
    j += i
    print(j)

print('----------------(8table)------------------')
# 7) Generate the Series... 8 16 24 32 40 48...80.
for i in range(8,81,8):
    print(i)

print("--------------Fibonacci series------------")
# 8) Generate the Series... 0 1 1 2 3 5 8 13 21
a = 0
b = 1
for i in range(9):
    print(a)
    c = a + b
    a = b
    b = c
    
print('--------------(Squar of each no )---------')
# 9) Generate the series... 1 4 9 16 25 36 49 64 81
for i in range(1,9):
    print(i * i)

print('----------------(3-table)------------------')
# 10) Generate the series... 3 6 9 12 15 18 21 24 27 30.
for i in range(3,31,3):
    print(i)

print('----------------(7-table)------------------')
# 11) Generate the Series... 7 14 21 28 35 42 49 56 63 70.
for i in range(7,71,7):
    print(i)

print('----------------(8table)------------------')
# 12) Generate the Series...  4 8 12 16 20 24 28 32 36 40.
for i in range(4,41,4):
    print(i)

print('----------------(8table)------------------')
# 13) Generate the Series... 10 20 30 40 50 60 70 80 90 100.
for i in range(10,101,10):
    print(i)

print('----------------(1 2 3 4 5 4 3 2 1)------------------------')
# 14) Generate the Series... 1 2 3 4 5 4 3 2 1.
for i in range(1,6):
    print(i, end=' ')
for i in range(4,0,-1):
    print(i,end=' ')

print('\n')


print('--------------------(6 table)--------------')
# 15) Generate the Series... 6  12 18 24 30 36 42 48 54 60
for i in range(6,61,6):
    print(i)