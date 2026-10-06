# #reverse the lines in a file
# f=open("k.txt","r")
# content=f.readlines()
# content.reverse()
# f=open("k.txt","w")
# f.writelines(content)
# f.close()

# # A file total_students.txt contains the names of all students in a class,
# # and a file passed_students.txt contains the names of students who passed the exam.
# # Write a Python program to:
# # Read the names from both files.
# # Find the students who did not pass.
# # Write their names to a new file named failed_students.txt, one name per line.
# f=open('total_students.txt','r')
# a=open('passed_students.txt','r')
# con=f.readlines()
# con2=a.readlines()
# con[-1]= con[-1]+'\n'
# con2[-1]= con2[-1]+'\n'
# con3=[]
# b=open('failed_students.txt','w')
# for i in con:
#     if i not in con2:
#         b.write(i)



# # Two files, swiggy.txt and zomato.txt, contain the names of food items ordered from each platform.
# # Write a Python program to read words from swiggy.txt and zomato.txt, combine them, and count how many times each word appears. Store the result in a dictionary and print it
# z=open('zomato.txt','r')
# s=open('swiggy.txt','r')
# z_orders=z.read()
# s_orders=s.read()
# items=z_orders.split('\n')
# items.extend(s_orders.split('\n'))
# print(items)
# count={}
# for i in items:
#     count[i]=items.count(i)
# print(count)
# z.close()
# s.close()




# A file marks.txt contains the names and marks of students as shown below:
# Anu 80
# Rahul 65
# Meera 90
# Arun 70
# Write a Python program to read the file and write the names of students who scored more than 75 marks into a file named names.txt.

f=open("marks.txt","r")
content=f.readlines()
f1=open("names.txt","w")
for i in content:
    s=i.split()
    if(int(s[1])>75):
        f1.write(s[0]+'\n')

