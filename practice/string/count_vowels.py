# Write a Python program to count the number of vowels in a string.
str = 'HEllo World'
vowels = "aeiouAEIOU"
count = 0

for char in str:
    if char in vowels:
        count += 1
print(f"The count of Vowels in str : {count}")