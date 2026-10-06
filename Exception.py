# Exception is an error condition occurs during execution of a program
# if an exception occurs interpreter stops the execution of the program and shows an error message
#
# Types of exception
#
# -NameError
# -ValueError
# -TypeError
# -IndexError
# -KeyError
# -AttributeError
# -ModuleNotFoundError
# -FileNotFoundError
# -ZeroDivisionError

# try:
#     num1=int(input("Enter a number:"))
#     num2=int*input("Enter another number:")
#     r=num1/num2
#     print(r)
# except:
#     print("Division by zero error")
# else:#works if no error
#     print("Hai")
# finally:#works in both cases
#     print("Hello")


#MUlTIPLE EXCEPTION BLOCKS
#Syntax:

# try:
#     --normal code to execute
# except ExceptionType1:
#     --handling code
# except ExceptionType2:
#     --handling code
# except:
#     --handling code if any other exception occurs


# # write a program that takes a number as input from user and finds the factorial of that number
# # using math.factorial().use a try -except block to handle the value error if user inputs a
# # number/character input
# import math
# try:
#     num=int(input("Enter a number:"))
#     print(math.factorial(num))
# except:
#     print("Enter a positive integer")

# # Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
# # and division based on user choice. Handle invalid inputs and division by zero using exception handling.
# while(1):
#     print("1.Addition")
#     print("2.Subtraction")
#     print("3.Multiplication")
#     print("4.Division")
#     print("5.Exit")
#     ch=int(input("Enter your choice:"))
#     try:
#         num1=int(input("Enter first number:"))
#         num2=int(input("Enter second number:"))
#     except:
#         print("Enter Integers only")
#     else:
#         if ch==1:
#             print(f"Sum:{num1+num2}")
#         elif ch==2:
#             print(f"Difference:{num1-num2}")
#         elif ch==3:
#             print(f"Product:{num1*num2}")
#         elif ch==4:
#             try:
#                 print(f"Division:{num1/num2}")
#             except:
#                 print("Zero division error")
#         elif ch==5:
#             exit()





# # write a program to open a file (text file) in read mode
# # if the file does not exist catch the file exception print the error message file does not
# # exist
# try:
#     f=open("abc.txt","r")
#     print(f.read())
# except:
#     print("File does not exist")
