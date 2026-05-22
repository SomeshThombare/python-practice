# Write a Python program to remove duplicate characters from a string.
text = 'programming'
result = ''.join(dict.fromkeys(text))
print(result)

#join concept for remember
# str = ['a','b','c','d','e']
# str = 'sam'
# print(str,'=',' '.join(str),'using sapce')
# print(str,'=','-'.join(str),'using dash(-)')
# print(str,'=',','.join(str),'using comma(,)')

#Using a Loop and a Set 
text = 'somnath Thomabre'
seen = set()
result = []
for char in text:
    if char not in seen:
        seen.add(char)
        result.append(char)
print(''.join(result))

# Using a Simple "if not in" Loop
# text1 = 'programming'
# for char in text1:
#     if char not in result:
#         result += char
# print(result)