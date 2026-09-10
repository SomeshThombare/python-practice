# s1 = 'a'
# s1 = 'A'
# print(s1,type(s1))
# print(id(s1))

# print(ord(s1)) # return the unicode value of char like A = 65

# s2 = 65
# print(chr(s2)) # take as input int and convert into char

# s3 = 'ABC'
# print(type(s3))
# iter = s3.__iter__
# var = iter.next()
# print(ord(var))

# string class objects are immutable proof
s4 = 'hello'
print(s4,id(s4), type(s4))

s4 = s4 + 'world'
print(s4,id(s4),type(s4))

print('-------------------')
s5 = 'hellooo'
print(s5,id(s5),type(s5))

s5 = 'Hello world!!!'
print(s5,id(s5),type(s5))

x = "sam"
print(x.upper())
