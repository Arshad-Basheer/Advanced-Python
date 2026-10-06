# Programming paradigm
# 1. Procedural
# 2. OOP
# 3. functional
#
# Multi pradigm programming
# 1. Class
# --Class is the blue print for creating objects
# Eg: Car
#
# 2. Object
# --Real world entity that has same characteristics and behaviour as that of class

# syntax:
 # class classname:
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")
p=Person('Amal',23)
p.display()