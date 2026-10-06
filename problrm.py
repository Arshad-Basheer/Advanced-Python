##write a program to read a text file and displays the number of lines in a file
f=open("k.txt","r")
# lineno=f.readlines()
# print(len(lineno))

##write a program to display the number of words in a file
# words=f.read()
# print(words)
# print(len(words.split()))

##write a program to update the second line in a file
# cont=f.readlines()
# cont[1]="hi iam arshad\n"
# f=open("k.txt","w")
# f.writelines(cont)

# #write a program to display the last 5 lines in a file
# cont=f.readlines()
# print(cont[-5:])

# #program to search a particular word in a file
cont=f.read()
word=input("enter the word:")
if word in cont:
    print("yes")
else:
    print("no")
f.close()
## find the number of letters,digits,and spaces in a file
# content=f.read()
# al=0
# dig=0
# sp=0
# for i in content:
#     if i.isalpha():
#         al+=1
#     elif i.isdigit():
#         dig+=1
#     elif i.isspace():
#         sp+=1
# print(f"No of letters = {al}")
# print(f"No of digits = {dig}")
# print(f"No of spaces = {sp}")