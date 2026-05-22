# class Dog:
#     def speak(self):
#         print('Bark')

# class Cat:
#     def speak(self):
#         print('maou')

# # def make_sound(obj):
# #     obj.speak()

# # dog = Dog()
# # cat = Cat()
# # make_sound(dog)
# # make_sound(cat)

# animal = Cat()
# animal.speak()
# animal = Dog()
# animal.speak()


#this class is not correct
# class NUM:

#     def __add__(x,y):
#         print(x + y)

#     # def add(x,y,z=0):
#     #     print(x+y+z)

# n = NUM()
# n.add(10,20)
# # n.add(2,20,10)


class A:
    def __init__(self,x):
        self.x = x

    def __add__(self,other):
        return self.x + other.x
    
a0 = A(10)
a1 = A(20)

print(a0 + a1)
    