#SINGLE LEVEL INHERITANCE

# class Person:
#     def __init__(self):
#         self.name=input("Enter your name:")
#         self.age=int(input("Enter your age:"))
#     def showdetails(self):
#         print(f"Name:{self.name}")
#         print(f"Age:{self.age}")
# class Student(Person):
#     def __init__(self):
#         super().__init__()
#         self.rollno=int(input("Enter your roll no:"))
#     def studentdetails(self):
#         super().showdetails()
#         print(f"Roll no:{self.rollno}")
#
# s=Student()
# s.studentdetails()


# class Company:
#     def __init__(self):
#         self.cname=input("Enter Company name:")
#     def showdetails(self):
#         print(f"Company name:{self.cname}")
#
# class Employee(Company):
#     def __init__(self):
#         super().__init__()
#         self.eid=input("Enter Employee id:")
#         self.des=input("Enter designation:")
#         self.salary=int(input("Enter salary:"))
#     def getsalary(self):
#         print(f"Employee id:{self.eid}")
#         print(f"Salary:{self.salary}")
#     def showemployeedetails(self):
#         super().showdetails()
#         self.getsalary()
#         print(f"Designation:{self.des}")
#
# e=Employee()
# e.showemployeedetails()



