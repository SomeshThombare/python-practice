# 1] byte datatype
b = b'ABC  '
print(type(b),b)


print('A =',b[0],'B =',b[1],'C =',b[2], b[3]) # space = 32 
for x in b:
    print( x)

# print('--------------')


# ba = bytearray(b)
# ba[0] = 97 # b'ABC' --> 'aBC'
# print(type(b),b)
# print(type(ba),ba)


print('----------------------------')
b = bytes ([0,2,3,10,100,150,250,255])
print(b,type(b))
for x in b:
    print(x)
print('-----------------------------------------')

# 2] bytearray datatype

b = b'ABC  '
ba = bytearray(b)
ba[0] = 97 # b'ABC' --> 'aBC'
print(type(b),b)
print(type(ba),ba)

