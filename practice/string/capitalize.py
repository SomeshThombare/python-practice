# Write a program to capitalize the first letter of every word in a string.
str = 'welcoem to underworld '
print(str.capitalize())
print(str.title())

#usign cap word
import string
text = 'you are a losser'
print(string.capwords(text))

#using list comprehension
text = 'make evry word count'

result = ' '.join(word.capitalize()for word in text.split())
print(result)