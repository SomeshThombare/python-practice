# Write a program to count uppercase and lowercase letters in a string.
str = 'Hii I am Somnath'
total_count = len(str)
upper_count = 0
lower_count = 0
for char in str :
    if char.isupper():
        upper_count += 1
    if char.islower():
        lower_count += 1
print(f'Total_count :{total_count}')
print(f"Uppercase:{upper_count}")
print(f"Lowercase: {lower_count}")