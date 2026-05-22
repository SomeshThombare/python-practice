l1 = ['sam', 'jay', 'pavan','nayan']

print('l1 id :',id(l1), l1)

print('---------------------')
l1[2] = 'pavan baba'

l2 = l1
print('l2 id : ',id(l2), l2)

print('l1[2] : ',l1[2],id(l1[2]))
print('l2[2] : ',l2[2],id(l2[2]))

print('__________________________________')

