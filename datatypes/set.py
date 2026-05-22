# s = set()
# print(type(s))

# s1 = {10}
# print(type(s1))

# s2 = {}
# print(type(s2))

# print(dir(s))

# print(help(set.update))


s = set()
# print(id(s))

s.add(10)
s.add('Skills')
s.add('IT')
s.add(10.3)
s.add(True)

# print(s)

# print(id(s))
# for x in s:
#     print(x)

# remove element for set
# print('Befoore remove',s)
# s.remove(10)
# print('After remove',s)

print('------------------------')

# print('Befoore remove',s)
# s.pop()
# print('After remove',s)

s.add('IT')
# print(s)

s1 = {'java','python','c','python','.net'}

s2 = {'java','python','math', 'history'}

print('set s1:',s1)
print('set s2:',s2)

print('Differenc of s1 --> s2(s1-s2):',s1.difference(s2)) # retun c , .net
print('Difference of s2 --> s1(s2-s1):',s2.difference(s1)) # return math, histroy

print('union of s1 --> s2:',s1.union(s2)) #return  all lang nmes with unique and duplicated are remove
print('union of s2 --> s1',s2.union(s1))

print('------------------------------------------------')
print('Before clere s1 is :',s1)
s1.clear()
print('After clere s1 is :',s1)

# # how to change any varibale in set 
# but set is immutable but is not possible 
# optionL solution is 
# FIRSLY remove variable and add updated variabel

s5 = {'c','C++','java'}
print('before update',s5)

s5.remove('c')
s5.add('C')
print('After update:',s5)