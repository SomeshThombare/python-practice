# num = int(input('Enter the numebr :'))

# if(num % 2 == 0):
#     print(num,'The given numbr is Even ')
# else:
#     print(num, 'The number id odd')

#example 2
# fb_databse = {
#     'username' : 'sam',
#     'password' : 'sam@123'
# }

# user_name = input('Enter username: ')
# user_password = input('Enter u r password :')

# if(user_name == fb_databse['username'] and  user_password == fb_databse['password']):
#     print('welcome to Facebook, Home page')
# else:
#     print('Error: Invalid username or password, Login page')


#example 3 : Grade system

marks = int(input('Enter marks:'))

if (marks > 90 and marks <= 100):
    print('A+')
elif (marks > 80 and marks <= 90):
    print('A')
elif (marks > 70 and marks <= 80):
    print('B')
elif (marks < 70 and marks > 35):
    print('C')
elif (marks < 35) :
    print('Fail')
else:
    print('Enter valid marks')