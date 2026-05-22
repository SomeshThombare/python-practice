nums = [1,2,3,4,5]
mapped = map(lambda num: num * num, nums ) 
# print(list)
print(mapped) #pritnhe oject addrss'
result = list(mapped)
print(result)


list_num = [2,4,6,8]
mapped = map(lambda num : num + 2, list_num)
result = list(mapped)
print(result)

names = ['sam','somnath','samarth']
mapped = map(lambda name : name.upper(),names)
result = list(mapped)
print(result)