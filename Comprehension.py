# 1. LIST COMPREHENSION.......

# square =[x*x for x in range(5)]
# print(square)

  # with condition>>>>>

# evens = [x for x in range(10) if x%2 != 0]
# print(evens)

  # expression inside comprehension>>>>>>>

# result = ["EVEN" if x%2==0 else "ODD" for x in range(5)]
# print(result)

  # STRING OPERATIONs...

# names = ["mohit","pushpa","yoegsh","himanshu"]
# length =[len(name) for name in names]
# print(length)

# SET COMPREHENSION>>>>

# num = [1,2,2,3,4,3,]
# result = {x*x for x in num}
# print(result)

# DICTIONARY COMPREHENSION>>>>>>>

# square = {x:x*x for  x in range (6)}
# print(square)

# GENERATOR COMPREHENSION>>>>>>>

square = (x**2 for x in range(6))
for val in square:
    print(val)