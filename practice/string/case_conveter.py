# Write a program to convert lowercase characters to uppercase without using .upper().
def to_uppercase(text):
    result = ''
    for char in text:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

intput_str = 'hello python'
print(f"Original Str:{intput_str}")
print(f"Uppercase : {to_uppercase(intput_str)}")