# Write a program to print duplicate characters in a string.
text = 'Programming'
seen = []
duplicates = []

for char in text:
    if char in seen and char not in duplicates:
        duplicates.append(char)
    else:
        seen.append(char)
print(f"Duplicates characters: {duplicates}")
