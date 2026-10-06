# Write a menu-driven Python program using a class Student to perform the following operations:
#
# 1Add Student(roll no,name,marks)
# 2Update Marks
# 3Display All Student Details
# 4Search Student by Roll Number
# 5Delete Student
# 6Exit
# Store student records in a list and perform all operations using the student's roll number.


class Student:
    def __init__(self):
        self.sname=input("Enter student name:")
        self.rl=int(input("enter roll no:"))
        self.mark=int(input("enter mark:"))
    def update(self):
        self.mark=int(input("Enter new mark:"))
        print(f"Updated mark:{self.mark}")
    def showdetails(self):
        print(f"Name:{self.sname}")
        print(f"Roll no:{self.rl}")
        print(f"Mark:{self.mark}")
l=[]
while(1):
    print("Menu driven program")
    print("1. Add Student(roll no,name,marks)")
    print("2. Update Marks")
    print("3. Display All Student Details")
    print("4. Search Student by Roll Number")
    print("5. Delete Student")
    print("6. Exit")
    ch=int(input("Enter your choice:"))
    print()

    if ch==1:
        a=Student()
        l.append(a)
    elif ch==2:
        rno=int(input("Enter the roll no of student to change the mark:"))
        for i in l:
            if i.rl==rno:
                i.update()
    elif ch==3:
        for i in l:
            i.showdetails()
    elif ch==4:
        rno = int(input("Enter the roll no of student:"))
        for i in l:
            if i.rl == rno:
                i.showdetails()
    elif ch==5:
        rno = int(input("Enter the roll no of student to be deleted:"))
        for i in l:
            if i.rl == rno:
                l.remove(i)
    elif ch==6:
        exit()

