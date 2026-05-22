# f = open('r_plue.txt','w') #create file 
# f.write('This is r_plue file')
# f.close()

f = open('r_plue.txt','r+') #open the file in r+ mode
f.write('i remove the i_plue fiel ') #overite the f_plus.txt file
print(f.read())
f.close()

f = open('r_plue.txt','r')
data = f.read()
print(data) #print the r_plue file
f.close()


