# # define a class named person ,accept name and age from the user display the details by using show() method and create and object and call the method
#
# class Person:
#     def __init__(self):
#         self.name=input("Enter your name:")
#         self.age=int(input("Enter your age:"))
#     def show(self):
#         print(f"Name:{self.name}")
#         print(f"Age:{self.age}")
# p=Person()
# p1=Person()
# p.show()
# p1.show()

# #Define a class named Employee with the following details
# #data members : Empid,name,age,salary,designation,place
# #member methods: getsalary(),showpersonaldetails()
# #create two objects for the employee class and call the above member methods.
#
# class Employee:
#     def __init__(self):
#         self.empid=int(input("enter the employee id:"))
#         self.name=input("Enter name:")
#         self.age=int(input("Enter age:"))
#         self.salary=int(input("Enter salary:"))
#         self.des=input("Enter designation:")
#         self.place=input("Enter place:")
#     def getsalary(self):
#         print(f"Empid:{self.empid}")
#         print(f"Salary:{self.salary}")
#     def showpersonaldetails(self):
#         print(f"Name:{self.name}")
#         print(f"Age:{self.age}")
#         print(f"designation:{self.des}")
#         print(f"Place:{self.place}")
# p=Employee()
# p.getsalary()
# p.showpersonaldetails()
# p1=Employee()
# p1.getsalary()
# p1.showpersonaldetails()


# # Define a class name student with the following details:
# # Data members: sname,rollno,class,mark1,mark2,mark3
# # Member methods : calculate()- calculate the total and average
# #                  showdetails()-display the details of a student with average marks
# # Create one object for the class and call the above member methods
#
class Student:
    def __init__(self):
        self.sname=input("Enter student name:")
        self.rl=int(input("enter roll no:"))
        self.cls=input("enter class:")
        self.mark1=int(input("enter mark1:"))
        self.mark2 = int(input("enter mark2:"))
        self.mark3 = int(input("enter mark3:"))
    def calculate(self):
        self.total=self.mark1+self.mark2+self.mark3
        self.avg=self.total/3
    def showdetails(self):
        print(f"Name:{self.sname}")
        print(f"Roll no:{self.rl}")
        print(f"Class:{self.cls}")
        print(f"Average:{self.avg}")
p=Student()
p.calculate()
p.showdetails()


# # Define a class book with the following details descriptions
# # data members : bookname,book id ,author id, author name,price,book title
# # member methods : getauthorid(), getauthorname(), getbooktitile(), getprice(), setauthorname(), setbooktitle(), setprice()
#
#
# class Book:
#     def __init__(self):
#         self.bname = input("Enter book name:")
#         self.bid = input("Enter book id:")
#         self.aid = input("Enter author id:")
#         self.aname = input("Enter author name:")
#         self.price = input("Enter price:")
#         self.btitle = input("Enter book title:")
#     def getauthorid(self):
#         print(f"Author id :{self.aid}")
#     def getauthorname(self):
#         print(f"Author name:{self.aname}")
#     def getbooktitle(self):
#         print(f"Book title:{self.btitle}")
#     def getprice(self):
#         print(f"Book price:{self.price}")
#     def setauthorname(self):
#         self.aname = input("Enter new author name:")
#         self.getauthorname()
#     def setbooktitle(self):
#         self.btitle = input("Enter new book title")
#         self.getbooktitle()
#     def setprice(self):
#         self.price = input("Enter new price:")
#         self.getprice()
#
# b=Book()
# b.setauthorname()
# b.setbooktitle()
# b.setprice()


# Write a menu driven python program for a banking system using a class Account to perform the following operations
# 1. Create an account
# 2. Withdraw money
# 3. Deposit money
# 4. Display balance
# 5. Exit
#
# Store account details in a list and search accounts using the account number
# Display account not found if the account does not exist

class Account:
    def __init__(self):
        self.accno = int(input("Enter account number:"))
        self.accname = input("Ente account name:")
        self.balance = int(input("Enter account balance:"))
        print()
    def withdraw(self):
        self.amount = int(input("Enter withdrawal amount:"))
        self.balance-=self.amount
        self.showbalance()
    def deposit(self):
        self.amount = int(input("Enter deposit amount:"))
        self.balance += self.amount
        self.showbalance()
    def showbalance(self):
        print(f"Current balance:{self.balance}")
        print()
l=[]
while(1):
    print("Menu driven program")
    print("1. Create an Account")
    print("2. Withdraw money")
    print("3. Deposit money")
    print("4. Display balance")
    print("5. Exit")
    ch=int(input("Enter your choice:"))
    print()
    if ch==1:
        a=Account()
        l.append(a)
    elif ch==2:
        num=int(input("Enter your account number:"))
        for i in l:
            if i.accno==num:
                i.withdraw()
                break
        else:
            print("Account not found")
    elif ch==3:
        num = int(input("Enter your account number:"))
        for i in l:
            if i.accno==num:
                i.deposit()
                break
        else:
            print("Account not found")
    elif ch==4:
        num = int(input("Enter your account number:"))
        for i in l:
            if i.accno==num:
                i.showbalance()
                break
        else:
            print("Account not found")
    elif ch==5:
        exit()



