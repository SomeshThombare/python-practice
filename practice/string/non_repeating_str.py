# Write a program to find the first non-repeating character in a string.
def unique_char(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char,0) + 1

        for char in s:
            if counts[char] == 1:
                return char
        return None
    
print(unique_char('mumbai'))
print(unique_char('sswiss'))

#
# uisng collection .counter
from collections import Counter
def first_unique_char(s):
    counts = Counter(s)
    for char in s:
        if counts[char] == 1:
            return char
        return None
print(first_unique_char('abcc'))

# Using string.find() and string.rfind()
text = 'alphabet'
for char in text:
    if text.find(char) == text.rfind(char):
        print(f"first unique char: {char}")
        break
