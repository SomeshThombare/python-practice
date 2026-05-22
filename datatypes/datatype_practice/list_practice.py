#list of list :
ind = []

MH = []
KA = []

MH.append('solapur') #(set of set) when we set then use frozent ind = set()  mh = set()  mh.add('pune')  ind.add(frozenset(mg))
MH.append('Kolhapur')

KA.append('Kalburgi') 
KA.append('Vijapur')

# print(MH)
# print(KA)

ind.append(MH)
ind.append(KA)

print('MH',MH)
print('KA',KA)
print('INDIA',ind)

print('------------ALl states city names in ind--------------------')

for states in ind:
    print(states)

print('----------Cityes is KA--------------')
for city in KA:
    print(city)

print('-------------ALl city naemes--------------------')
for state in ind:
    for city in state:
        print(city)
    

print('-------------------------------set of list--------------------------------')
# ind = set()
ind = list()
MH = list()
KA = list()

MH.append('pune')
MH.append("satara")

KA.append('HUbalii')
KA.append('Balarii')

# ind.add(tuple(MH))
# ind.add(tuple(KA))
ind.append(MH)
ind.append(KA)

print('MH',MH)
print('KA',KA)
print('INDIA',ind)
print('----------------------------------------')
print(MH[0],'--->',MH[1])
print(KA[0],'--->',KA[1])
print(ind[0],'--->',ind[1])
print(ind[0][0],'--->',ind[0][1])
print(ind[1][0],'--->',ind[1][1])

ind[1][1] = 'Benglore'
print(ind[1][0],'--->',ind[1][1])
print(ind)

# ind.remove(ind[0][1])
# print(ind)