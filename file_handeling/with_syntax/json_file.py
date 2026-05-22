import json
data = {
    'name' : 'sam',
    'age' : 25,
    'subject' : 'python'
}

print(data)
with open('data.json','w') as file:
    json.dump(data,file)

with open('data.json','r')as file:
    data = json.load(file)
    print(data)
 