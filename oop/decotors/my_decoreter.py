def my_decorator(fun):

    def wrapper():
        print(f"before execution of original functionL= : {fun.__name__}")
        fun()
        print(f'after exexution og original function :{fun.__name__}')
    return wrapper

@my_decorator
def say_hii():
    print('Hey, hello')

#when we create decorator then function call is not required
# func = my_decorator(say_hii)
# # print(func.__name__)
# func()

say_hii() # pass fun in my_decorator