# DUMPS.... it is converting python object into json string....

# import json

# student = {
#     "name":"mohit",
#     "age": 21,
#     "is_student":True
# }

# data = json.dumps(student,indent=4,sort_keys=True)

# print(data)
# print(type(data))

# LOADS()........ it is converting json string into python object....

# import json

# json_str = '''
# {
#     "name" :"mohit",
#      "age" :21
# }'''

# data = json.loads(json_str)
# print(data)
# print(type(data))

# DUMP()......... used to write json directly into a file....

# import json

# student = {
# "name":"mohit chaudhary",
# "city":"mathura",
# "age":21
# }

# with open ("student.json","w") as file:
#     json.dump(student,file,indent=4)

# #LOAD().........used to read json from file....

# with open ("student.json","r") as file:
#     data = json.load(file)

# print(data)
# print(type(data))

# FINAL EXAMPLE>>>>>>

import json

student = {
    "name":"Mohit", "age":21,
    "skills":["Python","SQL", "Machine Learning" ]
    }



with open("student.json","w") as file:

    json.dump(student,file,indent=4)



with open("student.json","r") as file:

    data = json.load(file)

print(data)

print(data["name"])

print(data["skills"][2])