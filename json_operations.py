import json

# f=open("sample3.json","r")
# content=json.load(f)
#
# print(content)

data=[
    {"name":"arun","age":20},
    {"name":"amal","age":22}
]

f=open("sample3.json","w")
json.dump(f,data)