# map of set of list of string 
world = {}

world['india'] = 'india'
world['japan'] = 'japan'

india = ('MH', 'MP')
MH = ['pune','Mumbai']
MP = ['Bhopal','Indore']
print('MH',MH)
print('MP',MP)
print('IND',india)

japan = ('State1', 'State2')
print('Japan',japan)

world['india'] = ('MH','MP')
world['japan'] = ('State1','State2')
print('World',world) 