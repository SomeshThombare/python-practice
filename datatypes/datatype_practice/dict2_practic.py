# write the map programfor map of map of map of list of string.

world = {}

# india 
ind = {}

MH = {}
MP = {}

MH['pune'] = ['Karvenage','Akurdi']
MH['Mumbai'] = ['Dadhar','Thane']

MP['Bhopal'] = ['A1','A2']
MP['Indore'] = ['A3','A4']

print('MH',MH)
print('MP',MP)

#japan
japan = {}

S1 = {}
S2 = {}

S1['city1'] = ['A5','A6']
S2['city2']  = ['A7','A8']
print('State1',S1)
print('State2',S2)

ind['MH'] = 'MH'
ind['MP'] = 'MP'
print('INDIA',ind)

japan['S1'] = 'S1'
japan['S2'] = 'S2'
print('JAPAN',japan)

world['ind'] = 'ind'
world['japan'] = 'japan'
print('World',world)


world['ind']['MH']['pune'] = 'pak'
print(world)