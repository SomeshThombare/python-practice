# Write a program to find the frequency of each character in a string.
#using dict
text = 'somnath Thombare'
text = 'sam'
frequency = {}
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)

#using collections.Counter
from collections import Counter
text = 'sam'
frequency = Counter(text)
print(frequency)

# Using a Dictionary Comprehension
text = 'dixt'
frequency = {char: text.count(char)for char in set(text)}
print(frequency)