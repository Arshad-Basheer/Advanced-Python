# # 1.Create a class named Circle with an attribute radius. Use a constructor to initialize the radius by accepting input from the user. Define the following methods:
# #
# # getarea() – to calculate and display the area of the circle.
# # getperimeter() – to calculate and display the perimeter (circumference) of the circle.
# #
# # Create an object of the Circle class and call both methods to display the results.
#
# class Circle:
#     def __init__(self):
#         self.r = int(input("Enter the radius of the circle:"))
#     def getarea(self):
#         self.area = 3.14*self.r**2
#         print(f"Area of the circle: {self.area}")
#     def getperimeter(self):
#         self.peri = 2*3.14*self.r
#         print((f"Perimeter of the circle: {self.peri}"))
# c=Circle()
# c.getarea()
# c.getperimeter()



# 2.Create a class named Account with attributes acctnumber, acctname, and balance. Initialize these values using a constructor by taking input from the user. Define the following methods:
#
# withdraw() – to withdraw an amount from the account and update the balance.
# deposit() – to deposit an amount into the account and update the balance.
# showbalance() – to display the current balance of the account.
#
# Create an object of the class and call the methods to perform withdrawal and deposit operations and display the updated balance.

class Account:
    def __init__(self):
        self.accno = int(input("Enter account number:"))
        self.accname = input("Ente account name:")
        self.balance = int(input("Enter account balance:"))
    def withdraw(self):
        self.amount = int(input("Enter withdrawal amount:"))
        self.balance-=self.amount
    def deposit(self):
        self.amount = int(input("Enter deposit amount:"))
        self.balance += self.amount
    def showbalance(self):
        print(f"Current balance:{self.balance}")

a=Account()
b=Account()
l=[a,b]
for i in l:
    print(f"Account number:{i.accno} Name:{i.accname}")