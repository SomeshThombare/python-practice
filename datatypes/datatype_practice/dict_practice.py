ind = {}

mh = {}
ka = {}

mh['pune'] = 'pune'
mh['solapur'] = 'solapur'

ka['bidhar'] = 'bidhar'
ka['mandya'] = 'mandya'

ind['mh'] = mh
ind['ka'] = ka

print('mh',mh) # mh {'pune': 'pune', 'solapur': 'solapur'}
print('ka',ka) # ka {'bidhar': 'bidhar', 'mandya': 'mandya'}
print('India ',ind) # India  {'mh': {'pune': 'pune', 'solapur': 'solapur'}, 'ka': {'bidhar': 'bidhar', 'mandya': 'mandya'}}

print('---------------------------------------------------------------')
# accesing the inner dict
print(ind['mh'])
print(ind['ka'])

print('-------------------------------------------')
# accessisng o innner dict data
print(ind['mh']['pune'])
print(ind['mh']['solapur'])
print(ind['ka']['bidhar'])

# print('--------using for loop-----------------------------------')
# for state in ind:
#     print(state)

# for states in ind.values():
#     for city in states.values():
#         print(city)
    
# updating te value
print('-----------update tha value------------------')
ind['mh']['pune'] ='MH12'
print(ind)

print('-----------delte the value--------------------')
# deletign the values
del ind['mh']['pune']
print(ind)