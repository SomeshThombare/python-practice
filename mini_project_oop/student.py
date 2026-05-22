#use OOP, class,oject, reference varibale, encapsulation, association (HAs -A - relation)
#Student has name, age, roll_no, Address and AdharCard
#Adress has city_name, tal_name, pin_code
#Adharcard has name, dob, adharNumber

class Student:
    def __init__(self,name, age, roll_no, address, adhar_card):
        self.__name = name
        self.__age = age
        self.__roll_no = roll_no
        self.__address = address
        self.__adhar_card = adhar_card
# gettrs 
    def get_name(self):
            return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_roll_no(self):
        return self.__roll_no
    
    #setter
    def set_name(self,name):
        self.__name = name

    def set_age(self,age):
        self.__age = age

    def set_roll_no(self,roll_no):
        self.__roll_no = roll_no


    # def display_studetnt_info(self):
    #     print(f'Student Name : {self.name}')
    #     print(f'student Age : {self.age}')
    #     print(f'Student roll NO : {self.roll_no}')
    #     self.address.display_address()
    #     self.adhar_card.display_AdharCard()

class Adress:
    def __init__ (self,city_name, tal_name, dist_name,pin_code):
        self.__city_name = city_name
        self.__tal_name = tal_name
        self.__dist_name = dist_name
        self.__pin_code = pin_code

    def get_city_name(self):
        return self.__city_name
    
    def get_tal_name(self):
        return self.__tal_name
    
    def get_dist_name(self):
        return self.__dist_name
    
    def get_pincode(self):
        return self.__pin_code
    
    #setters
    def set_city_name(self,city_name):
        self.__city_name = city_name
    
    def set_tal_name(self,tal_name):
        self.__tal_name = tal_name

    def set_dist_name(self, dist_name):
        self.__dist_name = dist_name

    def set_pincode(self,pincode):
        self.__pincode = pincode 


    # def display_address(self):
    #     print(f'Student City : {self.city_name}')
    #     print(f"Student Taluka : {self.tal_name}")
    #     print(f"Student Distict: {self.dist_name}")
    #     print(f"Student Pincode : {self.pin_code}")
   


class Adharcard:
    def __init__(self,name, dob, adharNumber):
        self.__name = name
        self.__dob = dob
        self.__adharNumber = adharNumber

    
    def get_name(self):
        return self.__name
    
    def get_dob(self):
        return self.__dob
    
    def get_adhar(self):
        return self.__adharNumber
    
    #setter
    def set_name(self,name):
        self.__name = name 

    def set_dob(self,dob):
        self.__dob = dob 

    def set_adhar(self,adharNumber):
        self.__adharNumber = adharNumber

        
    
    # def display_AdharCard(self):
    #     print(f"student adharCard name: {self.name}")
    #     print(f"Student DOB : {self.dob}")
    #     print(f"Student AdharCard NO : {self.adharNumber}")

# add = Adress('Katraj', 'Pune','pune', '413126')
# a_card = Adharcard('sam','24/09/2004','123456789')      
# s = Student("Sam",21,64,add, a_card)
# s.display_studetnt_info()
# # print(s.display_studetnt_info())



add = Adress('Katraj', 'Pune', 'Pune', '413126')

a_card = Adharcard('Sam', '24/09/2004', '123456789012')

s = Student("Sam", 21, 64, add, a_card)

# Accessing data using Getters 
print("--- Student Details ---")
print(f"Name: {s.get_name()}")
print(f"Age: {s.get_age()}")

# Accessing associated Address object data
print(f"City: {add.get_city_name()}")
print(f"Taluka Name: {add.get_tal_name()}")
print(f"District Nane: {add.get_dist_name()}")
print(f"Pincode: {add.get_pincode()}")

# Accessing associated Adharcard object data
print(f"Adhar Number: {a_card.get_adhar()}")
print(f"Date of Birth : {a_card.get_dob()}")
