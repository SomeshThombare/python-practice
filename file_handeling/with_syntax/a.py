with open('demp.txt','w') as f:
    f.write('i writing python code')

with open('demp.txt','r') as f:
    data =  f.read()
    print(data)

with open('demp.txt','w')as f:
    f.write('New Data')

with open('demp.txt','r') as f:
    data = f.read()
    print(data)

