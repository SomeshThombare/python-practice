nums = [1,2,3,4,5,6,7,8]
is_filtered = filter(lambda num : num % 2 == 0, nums)

even_nums = list(is_filtered)
print(even_nums)

is_filtered = filter(lambda num: num % 2 != 0, nums)
odd_nums = list(is_filtered)
print(odd_nums)

number = [1,2,3,4,5]
res = list(map(lambda x : x * 10, filter(lambda x : x > 3,number)))
print(res)