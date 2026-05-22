# using buitlin-fun
str = 'Hello world'
reversed_text = "".join(reversed(str))
print(reversed_text)

# using for loop
text = 'hello'
reversed_text = ''
for char in text:
    reversed_text = char + reversed_text
print(reversed_text)


# using while loop
text = 'sam'
reversed_text = ''
index = len(text) - 1
while index >= 0:
    reversed_text += text[index]
    index -= 1
print(reversed_text)


# using recursion 
def reverse_str(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse_str(s[:-1])
print(reverse_str("rohit"))