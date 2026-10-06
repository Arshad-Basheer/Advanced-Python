

# # 1.Create a class named Movie with attributes moviename,year,language,director,rating
# # and methods display_details() and update_rating()

# class Movie:
#     def __init__(self):
#         self.movie_name= input("Enter Movie Name: ")
#         self.movie_year= input("Enter Movie Year: ")
#         self.movie_language= input("Enter Movie Language: ")
#         self.movie_director= input("Enter Movie Director: ")
#         self.movie_rating= input("Enter Movie Rating: ")
#     def display_details(self):
#         print("Movie Name :",self.movie_name)
#         print("Movie Year :",self.movie_year)
#         print("Movie Language :",self.movie_language)
#         print("Movie Director :",self.movie_director)
#         print("Movie Rating :",self.movie_rating)
#     def update_rating(self):
#         self.movie_rating= input("Enter new Movie Rating: ")
#         self.display_details()
# M=Movie()
# M.display_details()
# M.update_rating()




# # 2.Create a Python program using Hierarchical Inheritance for a vehicle management system.
# #
# # Create a parent class Vehicle with the attributes brand, model, color, and year.
# # Add a method display() in the Vehicle class to display these details.
# # Create two child classes:
# # Car with an additional attribute mileage
# # Bike with an additional attribute cc
# # Override the display() method in both child classes to display the vehicle details along with their respective additional attributes.
# # Create objects of both classes, accept input from the user, and display the details.

# class Vehicle:
#     def __init__(self):
#         self.brand= input("Enter the Vehicle Brand : ")
#         self.model= input("Enter the Vehicle Model : ")
#         self.colour= input("Enter the Vehicle Colour : ")
#         self.year= input("Enter the Vehicle Year : ")
#     def display(self):
#         print("Brand :",self.brand)
#         print("Model :",self.model)
#         print("Colour :",self.colour)
#         print("Year :",self.year)
#
# class car(Vehicle):
#     def __init__(self):
#         Vehicle.__init__(self)
#         self.mileage= input("Enter the Mileage : ")
#     def display(self):
#         Vehicle.display(self)
#         print("Mileage :",self.mileage)
#
# class bike(Vehicle):
#     def __init__(self):
#         Vehicle.__init__(self)
#         self.cc= input("Enter the cc : ")
#     def display(self):
#         Vehicle.display(self)
#         print("CC :",self.cc)
# c=car()
# b=bike()
# c.display()
# b.display()






# # 3. Create an abstract class Employee with an abstract method calculate_salary()
# # create two subclasses
# # -FullTimeEmployee
# # -PartTimeEmployee
# # Each class should calculate salary differently.

# from abc import abstractmethod
# class Employee(ABC):
#     @abstractmethod
#     def calculate_salary(self):
#         pass
#
# class FulltimeEmployee(Employee):
#     def __init__(self):
#         self.rate=float(input("Enter employee salary rate per hour: "))
#         self.hours=int(input("Enter hours worked"))
#     def calculate_salary(self):
#         self.fsalary = (self.rate*self.hours)
#         print("Salary =", self.fsalary)
# class ParttimeEmployee(Employee):
#     def __init__(self):
#         self.rate=float(input("Enter employee salary rate per hour: "))
#         self.hours=int(input("Enter hours worked "))
#     def calculate_salary(self):
#         self.psalary = (self.rate*self.hours)
#         print("Salary =", self.psalary)
# print("Fulltime")
# f=FulltimeEmployee()
# f.calculate_salary()
# print("Parttime")
# p=ParttimeEmployee()
# p.calculate_salary()




# # 4. Create an abstract class Shape with abstract methods get_area() and get_perimeter()
# # create two subclasses
# #  -Rectangle
# #  -Square
# #
# #  -Each class should calculate area() and perimeter() differently.

# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def get_perimeter(self):
#         pass
#     @abstractmethod
#     def get_area(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self):
#         self.length = float(input("Enter length: "))
#         self.width = float(input("Enter width: "))
#     def get_area(self):
#         area = self.length * self.width
#         print("Area =", area)
#     def get_perimeter(self):
#         perimeter = 2 * (self.length + self.width)
#         print("Perimeter =", perimeter)
# class Square(Shape):
#     def __init__(self):
#         self.side = float(input("Enter side: "))
#     def get_area(self):
#         area = self.side * self.side
#         print("Area =", area)
#     def get_perimeter(self):
#         perimeter = 4 * self.side
#         print("Perimeter =", perimeter)
# print("Rectangle")
# r=Rectangle()
# r.get_area()
# r.get_perimeter()
#
# print()
#
# print("Square")
# s=Square()
# s.get_area()
# s.get_perimeter()





# # 5.Create a Python program using Object-Oriented Programming (OOP) that includes the following:
# # • Class: Course
# # Attributes:
# # course_name
# # instructor
# # duration
# # Methods:
# # show_course() → to display course details
# # • Subclass: Student (inherits from Course)
# # Additional attributes:
# # name
# # roll_no
# # marks
# # Methods:
# # show_student() → to display student details along with course details
# # get_result() → return "Pass" if marks ≥ 50, otherwise "Fail"
# # Create at least one object of the Student class
# # Display all details and result

# class course:
#     def __init__(self):
#         self.course_name = input("Enter course name: ")
#         self.instructur=input("Enter instructur: ")
#         self.duration = input("Enter duration: ")
#     def show_course(self):
#         print("Course name is ",self.course_name)
#         print("Instructor is ",self.instructur)
#         print("Duration",self.duration)
#
# class Student(course):
#     def __init__(self):
#         course.__init__(self)
#         self.name = input("Enter Student name: ")
#         self.rollno = input("Enter roll no: ")
#         self.marks = int(input("Enter marks: "))
#     def show_student(self):
#         course.show_course(self)
#         print("Student name is ",self.name)
#         print("Roll no is ",self.rollno)
#         print("Marks is ",self.marks)
#     def get_result(self):
#         if self.marks >=50:
#             print("pass")
#         else:
#             print("fail")
# s=Student()
# s.show_student()
# s.get_result()




# # 6.Create a Python program using Object-Oriented Programming (OOP) that includes a class called Employee with attributes such as id, name, age, designation, experience (in years), and salary. The class should include methods to display employee details and update the designation.
# # It should also include a method to check promotion eligibility where an employee is eligible for promotion if experience is 5 years or more and age is above 30; otherwise, the employee is not eligible.
# # Create at least one object of the Employee class, assign values directly, and display all the details along with the promotion eligibility result.
#
# class Employee:
#     def __init__(self):
#         self.id = input("Enter employee id: ")
#         self.name = input("Enter employee name: ")
#         self.age = int(input("Enter employee age: "))

# # 1.Create a class named Movie with attributes moviename,year,language,director,rating
# # and methods display_details() and update_rating()

# class Movie:
#     def __init__(self):
#         self.movie_name= input("Enter Movie Name: ")
#         self.movie_year= input("Enter Movie Year: ")
#         self.movie_language= input("Enter Movie Language: ")
#         self.movie_director= input("Enter Movie Director: ")
#         self.movie_rating= input("Enter Movie Rating: ")
#     def display_details(self):
#         print("Movie Name :",self.movie_name)
#         print("Movie Year :",self.movie_year)
#         print("Movie Language :",self.movie_language)
#         print("Movie Director :",self.movie_director)
#         print("Movie Rating :",self.movie_rating)
#     def update_rating(self):
#         self.movie_rating= input("Enter new Movie Rating: ")
#         self.display_details()
# M=Movie()
# M.display_details()
# M.update_rating()




# # 2.Create a Python program using Hierarchical Inheritance for a vehicle management system.
# #
# # Create a parent class Vehicle with the attributes brand, model, color, and year.
# # Add a method display() in the Vehicle class to display these details.
# # Create two child classes:
# # Car with an additional attribute mileage
# # Bike with an additional attribute cc
# # Override the display() method in both child classes to display the vehicle details along with their respective additional attributes.
# # Create objects of both classes, accept input from the user, and display the details.

# class Vehicle:
#     def __init__(self):
#         self.brand= input("Enter the Vehicle Brand : ")
#         self.model= input("Enter the Vehicle Model : ")
#         self.colour= input("Enter the Vehicle Colour : ")
#         self.year= input("Enter the Vehicle Year : ")
#     def display(self):
#         print("Brand :",self.brand)
#         print("Model :",self.model)
#         print("Colour :",self.colour)
#         print("Year :",self.year)
#
# class car(Vehicle):
#     def __init__(self):
#         Vehicle.__init__(self)
#         self.mileage= input("Enter the Mileage : ")
#     def display(self):
#         Vehicle.display(self)
#         print("Mileage :",self.mileage)
#
# class bike(Vehicle):
#     def __init__(self):
#         Vehicle.__init__(self)
#         self.cc= input("Enter the cc : ")
#     def display(self):
#         Vehicle.display(self)
#         print("CC :",self.cc)
# c=car()
# b=bike()
# c.display()
# b.display()






# # 3. Create an abstract class Employee with an abstract method calculate_salary()
# # create two subclasses
# # -FullTimeEmployee
# # -PartTimeEmployee
# # Each class should calculate salary differently.

# from abc import abstractmethod
# class Employee(ABC):
#     @abstractmethod
#     def calculate_salary(self):
#         pass
#
# class FulltimeEmployee(Employee):
#     def __init__(self):
#         self.rate=float(input("Enter employee salary rate per hour: "))
#         self.hours=int(input("Enter hours worked"))
#     def calculate_salary(self):
#         self.fsalary = (self.rate*self.hours)
#         print("Salary =", self.fsalary)
# class ParttimeEmployee(Employee):
#     def __init__(self):
#         self.rate=float(input("Enter employee salary rate per hour: "))
#         self.hours=int(input("Enter hours worked "))
#     def calculate_salary(self):
#         self.psalary = (self.rate*self.hours)
#         print("Salary =", self.psalary)
# print("Fulltime")
# f=FulltimeEmployee()
# f.calculate_salary()
# print("Parttime")
# p=ParttimeEmployee()
# p.calculate_salary()




# # 4. Create an abstract class Shape with abstract methods get_area() and get_perimeter()
# # create two subclasses
# #  -Rectangle
# #  -Square
# #
# #  -Each class should calculate area() and perimeter() differently.

# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def get_perimeter(self):
#         pass
#     @abstractmethod
#     def get_area(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self):
#         self.length = float(input("Enter length: "))
#         self.width = float(input("Enter width: "))
#     def get_area(self):
#         area = self.length * self.width
#         print("Area =", area)
#     def get_perimeter(self):
#         perimeter = 2 * (self.length + self.width)
#         print("Perimeter =", perimeter)
# class Square(Shape):
#     def __init__(self):
#         self.side = float(input("Enter side: "))
#     def get_area(self):
#         area = self.side * self.side
#         print("Area =", area)
#     def get_perimeter(self):
#         perimeter = 4 * self.side
#         print("Perimeter =", perimeter)
# print("Rectangle")
# r=Rectangle()
# r.get_area()
# r.get_perimeter()
#
# print()
#
# print("Square")
# s=Square()
# s.get_area()
# s.get_perimeter()





# # 5.Create a Python program using Object-Oriented Programming (OOP) that includes the following:
# # • Class: Course
# # Attributes:
# # course_name
# # instructor
# # duration
# # Methods:
# # show_course() → to display course details
# # • Subclass: Student (inherits from Course)
# # Additional attributes:
# # name
# # roll_no
# # marks
# # Methods:
# # show_student() → to display student details along with course details
# # get_result() → return "Pass" if marks ≥ 50, otherwise "Fail"
# # Create at least one object of the Student class
# # Display all details and result

# class course:
#     def __init__(self):
#         self.course_name = input("Enter course name: ")
#         self.instructur=input("Enter instructur: ")
#         self.duration = input("Enter duration: ")
#     def show_course(self):
#         print("Course name is ",self.course_name)
#         print("Instructor is ",self.instructur)
#         print("Duration",self.duration)
#
# class Student(course):
#     def __init__(self):
#         course.__init__(self)
#         self.name = input("Enter Student name: ")
#         self.rollno = input("Enter roll no: ")
#         self.marks = int(input("Enter marks: "))
#     def show_student(self):
#         course.show_course(self)
#         print("Student name is ",self.name)
#         print("Roll no is ",self.rollno)
#         print("Marks is ",self.marks)
#     def get_result(self):
#         if self.marks >=50:
#             print("pass")
#         else:
#             print("fail")
# s=Student()
# s.show_student()
# s.get_result()




# # 6.Create a Python program using Object-Oriented Programming (OOP) that includes a class called Employee with attributes such as id, name, age, designation, experience (in years), and salary. The class should include methods to display employee details and update the designation.
# # It should also include a method to check promotion eligibility where an employee is eligible for promotion if experience is 5 years or more and age is above 30; otherwise, the employee is not eligible.
# # Create at least one object of the Employee class, assign values directly, and display all the details along with the promotion eligibility result.
#
# class Employee:
#     def __init__(self):
#         self.id = input("Enter employee id: ")
#         self.name = input("Enter employee name: ")
#         self.age = int(input("Enter employee age: "))
#         self.designation = input("Enter employee designation: ")
#         self.experience = int(input("Enter employee experience: "))
#         self.salary = input("Enter employee salary: ")
#     def display_emp_details(self):
#         print("Employee ID:", self.id)
#         print("Employee Name:", self.name)
#         print("Employee Age:", self.age)
#         print("Employee Designation:", self.designation)
#         print("Employee Experience:", self.experience)
#         print("Employee Salary:", self.salary)
#     def update_designation(self):
#         self.designation = input("Enter employee designation: ")
#         Employee.display_emp_details(self)
#     def check_eligibility(self):
#         if self.experience>=5 and self.age>30:
#             print("Employee is eligible")
#         else:
#             print("Employee is not eligible")
# e=Employee()
# e.display_emp_details()
# e.update_designation()
# e.check_eligibility()
#         self.designation = input("Enter employee designation: ")
#         self.experience = int(input("Enter employee experience: "))
#         self.salary = input("Enter employee salary: ")
#     def display_emp_details(self):
#         print("Employee ID:", self.id)
#         print("Employee Name:", self.name)
#         print("Employee Age:", self.age)
#         print("Employee Designation:", self.designation)
#         print("Employee Experience:", self.experience)
#         print("Employee Salary:", self.salary)
#     def update_designation(self):
#         self.designation = input("Enter employee designation: ")
#         Employee.display_emp_details(self)
#     def check_eligibility(self):
#         if self.experience>=5 and self.age>30:
#             print("Employee is eligible")
#         else:
#             print("Employee is not eligible")
# e=Employee()
# e.display_emp_details()
# e.update_designation()
# e.check_eligibility()