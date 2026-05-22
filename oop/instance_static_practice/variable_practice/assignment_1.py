"""Assignment 1: Student Management System

# Objective:
Understand class, object, variables, and methods in Python

# Problem Statement:
Create a class Student and implement the following:

# Requirements:
1. Variables:
Instance variables: name, age, marks

Class variable (static): school_name = "ABC School"

2. Methods:
Instance Method

display_details() → print student details

Class Method

change_school(cls, new_name) → change school name for all students

Static Method

is_pass(marks) → return True if marks ≥ 40 else False

3. Object Creation:
Create 3 student objects

Assign different data

Call all methods."""

class Student:
    #classs var
    school_name = "ABC School"

    def __init__(self,name, age, marks):
        """Instance variables: name, age, marks"""
        self.name = name
        self.age = age
        self.marks = marks

    def display_details(self):
        print('Student Name :',{self.name})
        print('Student age :',self.age)
        print('Student Marks:', self.marks)
        print('School Name:',Student.school_name)


    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

    @staticmethod
    def is_pass(marks):
        return marks >= 40
            

s = Student('Sam',21, 99)
s.display_details()
print('\n')

s1 = Student('Samarth', 21, 50)
s1.display_details()
print('\n')

s2 = Student('Somesh', 22, 29)
s2.display_details()
print('\n')

# Change school name
Student.change_school('SIT')

print("After changing school Name:")
print('\n')

s.display_details()
print("Sam is pass ?", Student.is_pass(s.marks))
print('\n')

s1.display_details()
print("Samarth is pass ?",Student.is_pass(s1.marks))
print('\n')

s2.display_details()
print("Somesh id pass ?", Student.is_pass(s2.marks))





