#All strig methods practuces here
s = 'skills it'
# s=[1]
# s=[-8]
# print(s)

#access usign +ve index through
# print(0,s[0])
# print(1,s[1])
# print(2,s[2])
# print(3,s[3])
# print(4,s[4])
# print(5,s[5])
# print(6,s[6])
# print(7,s[7])
# print(8,s[8])
# print('----------------------------------------------')

#access usign -ve index through
# print(-1,s[-1])
# print(-2,s[-2])
# print(-3,s[-3])
# print(-4,s[-4])
# print(-5,s[-5])
# print(-6,s[-6])
# print(-7,s[-7])
# print(-8,s[-8])


# s[1] = 'K' # Error --> is it not possible beacaseu the str in immutable
# 1] upper:-    creatate new string object 
            # - convert each char into upper case adn stored into new object 
print(s[1].upper())
str = 'Upper'
print(str.upper())
 
print('-------------------')
print('str id-->',id(str))
str = print('uppercase str id -->',id(str.upper()))
print('------------------------')

# 2] lower:-    creatate new string object 
            # - convert each char into lower case and stored into new object 
str = 'LOWER'
print(str,'=',str.lower())

# 3]capitalize
    #- 1st letter of 1st word in the sentence convert it upper case
str = 'i am a somnath'
print(str,'=',str.capitalize(),'using capitalize method')

#title -- same as capitalize but he convet every word of 1st letter
print(str,'=',str.title(),'using title metod')

# replace :- scan string , create new bufffer, copy + replace new buffer

str = 'somnath'
print(str,'=', str.replace('s','A'),'s--> A')

#6] split: iterate on string char
    # create new list object
    # store substring in a new list object
    # split return as output as list
print('___________')

name = 'SAM Thombare'
name =  name.split(' ') # return by ',' of each letter
print(name)

str = 's, a, m'
print(str,'=',str.split(',')) # return in the list

str = 'skills it academy pune'
print(str.split(' '))

#7] join : -calculate the size first
        #   - allocatet the memory once
        #   - copy the strings effieciently
        #   - join return in output as str
        #   - syntax:
                    # 'seperator'.join(list)

print('------------------------------------')
str = ['a','b','c','d','e']
print(str,'=',' '.join(str),'using sapce')
print(str,'=','-'.join(str),'using dash(-)')
print(str,'=',','.join(str),'using comma(,)')
print('----------------------------------------')
#8] strip():- scan left and right space
            # - create new object
            # - remove space and store string into new object

str = '      SAM   Thomabre                  '
print(str,'=',str.strip(),':-removed unwnated space in left side and right side of the str')
print("---------------------------------------------------------------------")

#9]length() :- return the total lenght of string 
            # - len is aslo a functon()
str = '123456'
print(str,'=',len(str))

# # slice : it will return new strign object
#          - if we want substring from a given strign then use slice opertor.
#           - substrign is part of strign  and if we want part of  strig use substring.
#          - SYNTSX : [VARIBALE_name[index] -- will get single char
            #             # variable_name [start_index : stop_index : step_value]
            # - NOTE:- default value for srart_index is 0
            #        - default value for stop_index is len(string) -1
#             #        - default value for step is +1
# working principle of slice
#     a] case-1 step value is  +ve
#        1] interpreter will create a pointer for start index and start traversign towords forword(+ve) direction till the stop -1 is found another pointer poit=ntign to stop -1 value. a
#         and retrn in between start and stop  poineer string.
#         if stop-1 value is not found then return '' empty string.

#     b] case-2 step value is  -ve
#        1] interpreter will create a pointer for start index and start traversign  towords backwords(-ve) direction till the stop -1 is found another pointer poitntign to stop -1 value. 
#         and retrn in between start and stop.
#         if stop-1 value is not found then return '' empty string.

       
str = 'somnath'
str =[]

