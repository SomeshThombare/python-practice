
#map list of string
ind = {}
ind['Mh'] = ('pune','Mumbai')
ind['MP'] = ('indore','indore')
print('INDIA',ind)

print('-------------------------set()---------------')

ind = []
Mh = set()
Mh.add('solapur')
Mh.add('Satara')
print("MH",Mh)

KA = set()
KA.add('Manyda')
KA.add('Mandya')
KA.add('BIdhar')
print('KA',KA)

ind.append(frozenset(Mh))
print('ind',ind)