s = frozenset({10,20,30,40,50})
print(type(s),id(s))

for x in s:
    print(x)
print('---------------------------------')
s1 = frozenset({10,20,30,50,70})

s2 = frozenset({10,20,50,60,100})

print('Differene of (s1-s2):',s1.difference(s2))

print('Difference of (s2-s1):',s2.difference(s1))

print('Union of s1 --> s2:',s1.union(s2))

print('Union of s2 --> s2:',s2.union(s1))