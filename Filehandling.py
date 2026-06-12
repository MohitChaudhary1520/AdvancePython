# read mode ()......

# file = open("student.txt" , "r")
# data = file.read()
# print(data)

# file.close()

# write mode.....

# file = open("student.txt", "w")
# file.write("hyy i am mohit i am fine what about you\n")
# file.close()

# file = open("student.txt", "r")
# data = file.read()
# print(data)
# file.close()

# aapend mode()..........

# file = open("student.txt", "a")
# file.write("hyy i am mohit i am fine what about you\n")
# file.close()

# file = open("student.txt", "r")
# data = file.read()
# print(data)
# file.close()

# creating new file......

# file = open("newfile.txt", "x")
# file.close()

# read oneline..........

# file = open("newfile.txt", "r")
# print(file.readline())
# file.close()

#read all line.........

# file = open("newfile.txt", "r")
# print(file.readlines())
# file.close()

# using with statement.........

with open("newfile.txt", "r") as file:
    data = file.read()

print(data)