print('Program start ')

# while 10 < 20 :
#     print('hello') # loop is gone infinite loop


a = 0
while a <= 10 : # termination condiion whwn loop variable value is 11 stop the loop
    print('hello')
    a +=1 
print('Program end ')

# hint For remembering the while loop
# I C U {
#  1] I ==> Initilizaton of loop variable
#  2] conditon 
# 3] updation of loop varibale }

# continue keyword
i = 1
while i <= 10:
    if i == 5:
        i+=1
        # continue #
        pass
    else:
        print(i)
    i = i+1
    print('hii')
print('program end')

print('-----------even print and odd skip-----------------')

print('start program')

i = 0
while i <= 10:
    if i % 2 != 0:
        #continou 
        pass
    else:
        print(i)
    i += 1
print('end program')



