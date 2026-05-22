str = 'sam' #false
str = 'markram' #true
is_palindrome = str == str[::-1]
print(is_palindrome)

#recursive function
def reverse_str(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse_str(s[:-1])
word = 'markram'
if word == reverse_str(word):
    print('it is palindrome!')
else:
    print('NOt a palindrome.')