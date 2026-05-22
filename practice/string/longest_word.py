# Write a Python program to find the longest word in a sentence.
sentence = ' I am pyton fullstack developer'
words = sentence.split()
longest_word = max(words,key= len)
print(f"The longest word is : {longest_word}")

longest = ''
for word in words:
    if len(word)> len(longest):
        longest = word
print(f"The longest word: {longest}")