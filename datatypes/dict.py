d3 = {'name':'sam',
      'marks':80,
      'rollno':10}
# print(d1)

d = {
    1 : 'jay',
    2 : 'pavan',
    3 : 'nayan',
    4 : 'kiran'
}

d1 = {
    1 : 'jay',
    2 : 'pavan',
    3 : 'nayan',
    4 : 'kiran'
}



# print(d)

# print(d[1]) # access values usign key

# print(d.get(1)) # acces values usign get method

# print('All keys in Dict : ',d.keys())  #it will return all keys

# print('All Values in dict  :',d.values()) # it will return all values

# print('all keys and values return :',d.items())

#del method
print('---------------------------------------------------')
print(d)
del d[1]
print(d)

print('------------------------------------------------')
# del d[4]
# print(d)

print('-------------------------------------------------')

#pop method
print(d1)
d1.pop(1)
print(d1)

print('----------------------------------------------------')

# print('Before clear :',d)
# d.clear()
# print('After clear :',d)

# single value update in dict
# print('id=d[2]:',id(d[2]))
# d[2] = 'pavan baba'
# print('id=d[2]',id(d[2]),d[2])
# print(d)

# how to update multiple update

# print('Before update :',d)
# d.update({
#     2:'pavan baba',
#     4 : 'kiran baba'
# })
# print('After update :',d)

# this is use wene u dont know values but u know about keys then use
my_keys  = {1,2,3,4,5,6}
my_student_dict = dict.fromkeys(my_keys, "NO student")

print('Before add student names',my_student_dict)

my_student_dict[1] = 'Sam'

my_student_dict[2] = 'Somnath' 
print(my_student_dict)

# print(my_keys.get(22,'unkown kwy'))

# list to dict convert 
my_list = [(1,'sam'), (2,'pavan'), (3,'nayan')]
my_dict = dict(my_list)
print(my_list)
print(my_dict)

#for loop
for key in d:
    print(key)
print('----------------------------')
for key in d.values():
    print(key)
print('----------------------------')
for value in d.values():
    print(value)
print('----------------------------')
for key, value in d.items():
    print(key, '---->',value)

print('---------------------pop and del deffer----------------------')
data = {'name': 'Alice', 'age': 25}

print(data['name'])
print(data['age'])

age = data.pop('age', 0)  # age = 25, 'age' is removed
print(data)

city = data.pop('city', 'Unknown')
print(city)

# city = data.pop('city', 'Unknown')  # Returns 'Unknown', no error

# # Use del if you just want to delete and are sure it exists
# del data['name']  # 'name' is removed
# # del data['city']  # This would crash with a KeyError!
