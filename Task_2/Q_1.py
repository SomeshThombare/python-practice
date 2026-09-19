# 1) Write a Program To print 1 to 25 nos.

r = range(1,26)
for i in r:
    print(i)

print('-----------25 --> 1 ----------')
# 2) Write a Program To print 25 to 1 nos.
r = range (25,0,-1)
for i in r:
    print(i)

print('--------------Odd nos----------')
# 3) Write a Program To print 1 to 100 Odd nos.
r = range(0,100)
for i in r:
    if (i % 2 != 0):
        print(i)

print('------Even Nos---------------')
# 4) Write a Program To print 1 to 100 even nos.
r = range(0,101)
for i in r:
    if (i % 2 == 0):
        print(i)
print('---------sum of 1--50 ------------------')
# 5) Write a Program To print sum of 1 to 50 Odd nos.
r = range(1,50)
result = 0
for i in r:
    if(i % 2 != 0):
        result += i
print('Sum of odd nos:',result)

# 6) Write a Program To print sum of 1 to 50 EVEN nos.
r = range(1,51)
result = 0
for i in r:
    if(i % 2 == 0):
        result += i
print('Sum of even nos:',result)
print('---------(-45 to 45 nos-------------------)')
# 7) Write a Program To print -45 to +45 nos. // negative no and positive no
r = range(-45, 46)
for i in r:
    print(i)
print('---------(50 to 100 nos-------------------)')
# 8) Write a Program To print 50 to 100 nos.
r = range(50, 101)
for i in r:
    print(i)

print('--------------sum of odd and even 1 to 100)----------------')
# 9) Write a Program To print sum of odd and even no.
r = range(0,101)

even_sum = 0
odd_sum = 0

for i in r:
    if(i % 2 == 0):
        even_sum += i
    else:
        odd_sum += i

print('Sum of even no's:',even_sum)
print('Sum of odd no's : ',odd_sum)

# 10) Write a Program To print even and odd No
r = range(0, 101)
for i in r:
    if(i % 2 == 0):
        print('Sum No',i)
    else:
        print('odd no',i)


print('----------(1 to 100 nos-----------)')
# 11) Write a Program To print 1 to 100 no.
r = range(0,101)
for i in r:
    print(i)

print('----------(100 tp 0 nos ------------)')



# 12) Write a Program To print 100 to 1 no.
r = range(101,0,-1)
for i in r:
    print(i)


print('--------------(30 to 50 Nos--------------)')
# 13) Write a Program To print 30 to 50 no.
r = range(30,51)
for i in r:
    print(i)


print('--------------(Even and odd nos 1 to 25 ----------)')
# 14) Write a Program To print count of even No 1 to 25 по.
count = 0
for i in range(1, 26):
    if i % 2 == 0:
        count += 1
print('Total count of even nos:',count)


# 15) Write a Program To print count of odd No 1 to 25 nos
count = 0
for i in range(1,26):
    if(i % 2 != 0):
        count += 1
print('Total count of odd nos:',count)
