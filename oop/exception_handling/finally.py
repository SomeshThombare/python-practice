# print('START')
# try:
#    print('try block')
#    print(10/0) # when comment thsi statement then  finlayy  block alwayes execute and  without commen theen except block ececute otherwise only try--finlayy execute

# except Exception as e:
#     print('Except block')
# finally:
#     print('finallly block')

# print('STOP')



# print('START')
# try:
#    print('file opne')
#    print('file operation , writing')
#    print(10/0) # when comment thsi statement then  finlayy  block alwayes execute and  without commen theen except block ececute otherwise only try--finlayy execute
#    print('other file operations')
# except Exception as e:
#     print('Except block')
# finally:
#     print('finallly block')

# print('STOP')

print('START')
print(1)
# print(10/0)

try:
    print(2)
    print(10/0)
except Exception as e:
    try:
        print(10/0)
    except Exception as e:
        print(2.1)
    print(3)

else:
    print(4)

finally:
    print(5)

print('End')