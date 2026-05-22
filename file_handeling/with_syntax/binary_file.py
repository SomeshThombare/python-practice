with open('nature.jpg','rb')as f:
    data = f.read()
    print(type(data))
    for x in data:
        print(x)

    print(type(data))