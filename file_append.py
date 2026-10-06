# f=open("k.txt","a")
# f.write('\npython')

# f=open("k.txt","a")
# f1=open("names.txt","r")
# f.write('\n')
# f.write(f1.read())

f=open("k.txt","a+")
f.write('hello')
f.seek(0)
f.write('hai')


