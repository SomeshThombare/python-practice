# Write a program to count how many times a substring appears in a string.
def count_substring(main_str, sub_str):
    count = 0
    main_len = len(main_str)
    sub_len  = len(sub_str)

    for i in range(main_len - sub_len + 1):
        if main_str[i : i + sub_len] == sub_str:
            count += 1

    return count
text = 'Hello Hello python Hello'
target = 'Hello'

result = count_substring(text, target)
print(f"The substring '{target}' appers {result} times.")