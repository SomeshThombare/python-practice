def print_nums(n1,n2,n3,**kwargs):
    print(type(kwargs))
    print(n1,n2,n3,kwargs)

print_nums(10, 20, 30, n4=40, n5=50)