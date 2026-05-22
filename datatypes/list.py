my_list = []

print(my_list)

my_list.append('Java')

my_list.append('python')

print(my_list)

my_list.insert(0,'Ruby')
print(my_list)

new_list = ['Math', 'English','Physcics']
# print(new_list)

# my_list.insert(0,new_list)
# print(my_list)

print('_________________________')
print('This is extend method')
my_list.extend(new_list)
print(my_list)

print('--------------------------')

# pop method
lang = ['Marathi','Hindi','English','Kannada']
print(lang)
lang.pop(2) # remove englilsh
print(lang)

print('---------------------------')
#hwo to check any  object in the lsit in which idx
lang = ['Marathi','Hindi','English','Kannada']
print(lang.index('Kannada')) # 3

lang = ['Marathi','Hindi','English','Kannada']
nums = [2,3,10,2,4,3,4,6,4,6]

# sort method use to sort in asc is default and u want to desc to user reverse= True
print("Before sorting :", lang)
lang.sort()
print('After Sorting:', lang)

#ascding order
# print("Before sorting :", nums)
# nums.sort()
# print('After Sorting:', nums)

# print('---------------------------------------')
# # revers the list # descinding order
# print('Before  Sorting :', nums)
# nums.sort(reverse=True)
# print('After sort :',nums)


# note teh given list is after sorted store in another list with differnt id
# nums = [2,3,10,2,4,3,4,6,4,6]
# print(id(nums),nums)
# new_nums = sorted(nums) #fucton
# print(id(new_nums),new_nums)

# using reverse method sort in descending order
# nums = [2,3,10,2,4,3,4,6,4,6]
# print(id(nums),'Before Sorting: ',nums)
# new_nums = sorted(nums, reverse=True) #fucton
# print(id(new_nums),'Aftr sorting :',new_nums)

print('------------------------------------')
lang = ['Marathi','Hindi','English','Kannada']

for i in lang :
    print(i)

    print('---------------------------')

# enumerate() function will return two objects first index and second list of object
# enumerate() function will return  iterator object so we acan use for-loop in enumerate object

for index, x in enumerate(lang): 
    print(index,x)