#Q1 
with open ('practice.txt','w')as f:
    f.write('Hii evryon\nnew learning file I/O\n')
    f.write('using java.\nI like programming in java.')

with open("practice.txt",'r')as f:
    data = f.read()
    # print(data)

#Q2
new_data = data.replace("java","Python")
print(new_data)


with open('practice.txt','w')as f:
    f.write(new_data)

#Q3 check learnifn is present or not ?
word = 'learning'
with open("practice.txt",'r')as f:
    data = f.read()
    if(data.find(word) != -1 ):
        print("Found")
    else:
        print('Not found')
        
#check the line no of word=learning?
def check_for_line():
    word = 'learning'
    data = True
    line_no = 1
    with open('practice.txt','r')as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return 
            line_no += 1
    return -1 

check_for_line()

#count the even nos
count = 0
with open('num.txt','r') as  f:
    data = f.read()
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
print('The even of count is: ',count)