users = {
    'sam@gmail.com' : {'username' : 'sam', 'email':'sam@gmail.com'  ,'password' : 'sam@123'},
    'jay@gmail.com' : {'username' : 'jay', 'email':'jay@gmail.com'  ,'password' : 'jay@123'},
}

# register new user

def create_user(username,email,password):
    return  {'username' : username, 'email':email  ,'password' : password}

#user/sign_up fun
def sign_up(username,email,password):
    if email in users:
        return 'user is already registerd'
    
    user = create_user(username,email,password)
    users [user['email']] = user
    return "User Regisetr Scuessfully..."

#user/sign_in fun
def sign_in(username,email,password):
    if  users.get(email)['email'] == email and users.get('password')['password'] == password:
        return 'Login successfully'
    return 'Userame or password is incorrect'

print(sign_up('sam','sam@gmail.com','sam@123')) # login user

print(sign_up('abhi','abhi@gmail.com','abhi@123')) # create user
print(users)

