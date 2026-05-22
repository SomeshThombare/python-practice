my_lang = ['java','py','c','c++']

my_iter = iter(my_lang)

print(type(my_iter))
""" workign of loop
f = my_iter.__next__() # 1s way  to write the iter
print(f)
print('-------------------------------')

fl1 = next(my_iter) # 2nd way to write the iter
print(fl1)

fl2 = next(my_iter)
print(fl2)

fl3 = next(my_iter)
print(fl3)

"""
#Example: --
my_num = {1,2,3,4,5,6}
result = 0
for num in my_num:
    result = result + num
    print('num:',num,'result:',result)
