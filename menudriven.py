def file_read():
    name=input("enter the file name")
    f=open(name,"r")
    content=f.read()
    print(content)

def file_write():
    name=input("enter the file name:")
    f=open(name,'w')
    content=input("enter the content to write:")
    f.write(content)

def file_append():
    name=input("enter the file name:")
    f=open(name,'a')
    content=input("enter the content to write:")
    f.write(content)

def file_search():
    name=input("enter the file name:")
    f=open(name,"r")
    content=f.read()
    se=input("enter the word:")
    if se in content:
        print("present")
    else:
        print("not present")

def file_remove():
    import os
    name=input("enter the file name:")
    os.remove(name)

while(1):
    print('1. File read')
    print('2. File write')
    print('3. File append')
    print('4. File search')
    print('5. File remove')
    print('6. Exit')

    ch=int(input("Enter your choice: "))

    if ch==1:
        file_read()
    elif ch==2:
        file_write()
    elif ch==3:
        file_append()
    elif ch==4:
        file_search()
    elif ch==5:
        file_remove()
    else:
        exit()