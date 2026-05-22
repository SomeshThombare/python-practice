f = open('w_plus.txt','w')
f.write('This is w_plue file ')
f.write('overite the w_plus file')
f.close()

f = open('w_plus.txt','r')
data = f.read()
print(data)
f.close()