def login_required(function):
    def wrapper():
        if 'sam' in session :
            function()
        else :
            print('Login first')
    return wrapper

session = { }


def login():
    session['sam'] = 'sam@123'
    print('Logn page')

@login_required
def home():
    print('Home page')

@login_required
def message():
    print('Message page')
    
@login_required
def post():
    print('post page')

home()
message()
