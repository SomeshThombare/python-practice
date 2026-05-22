t  = ()
# print(id(t),type(t))


# t1 = tuple()
# print(type(tuple))

# t2 = (1) # Thsis is not way to declare a tuple
# print(type(t2))

# t3 = type(1,)
# print(type(t3))


# print(dir(t))  # to check the methods of tuples


# print(help(tuple))  # to chacke the tuple info

t = ('Java','Pyton','c','cpp')

print('Lenght of Tuple',len(t))

print('How many times CPP in tupel available: ',t.count('cpp')) # the count method is used to count the any one object or valeu how many times preset in thsi tuple

print('The index No of C is',t.index('c'))


# t[3] = 'C++' # this is not valid : TypeError: 'tuple' object does not support item assignment
# print(t)

print('-------------------------------------')
for lang in t:
    print(lang)

print('---------------------------------')

t1 = ('Java','Pyton','c','cpp','.NET')

for index, langugage in enumerate(t1):
    print(index,langugage)
print('-------------------------------------------------------------')

# add two tuples
# in this case the interpeter is create a new object as t3 asn store the  t3 addres or output
t3 = t1 + t

# # print('t3"',t3)
# print('----------------------------------------------------------------------')
print('This is t :',id(t), t)
print('------------------------------------------------------------------')
print('This is t1: ',id(t1),t1)
print('---------------------------------------------------------------')
print('thsi is t3: ',id(t3),t3)
 

print('----------------')

# 1. Take user input for the number of terms (n)
n = int(input("Enter the number of terms: "))

# 2. Initialize the first two terms
a = 0
b = 1

print("Fibonacci Series:", end=" ")

# 3. Use the 'for' loop to calculate and print the series
for i in range(n):
    print(a, end=" ")
    
    # Using your specific condition breakdown:
    c = a + b   # Step 1: Calculate the new sum
    a = b       # Step 2: Move second term to the first position
    b = c       # Step 3: Move the new sum to the second position
