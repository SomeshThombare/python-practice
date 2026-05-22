# Write a Python program to sort characters of a string alphabetically.
text = 'python'
sorted_text = ''.join(sorted(text))

print(sorted_text)

text = 'alphabet'
result = ''.join(sorted(text, reverse=True))
print(result)