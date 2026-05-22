
#file open in write mode
f = open ('demo.txt','w')
f.write('I want to learn js')

f = open('demo.txt','a') #
f.write('\n I want move on react js')
f = open('demo.txt','r') #read thre file 
data = f.read() 
print(data) #printhe data
f.close()

#creatian  a new file with code
f =  open('sample.txt','a')
#wrtigng the data inthe sample.txt fiel
f.write('This is fiel handeling lecture ')
f.close()

#readign the file sample.txt file
f= open('sample.txt','r')
data  = f.read()
print(data)
f.close()