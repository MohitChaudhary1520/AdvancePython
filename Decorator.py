# python me function bhi object ki trh behave krta h 

# def greet():
#     print("hyy pushpa")

# a = greet
# a()

# function ke andar function ye foundation h decorator kii........

# def outer():

#     def inner():
#         print("inner function")

#     inner()

#     print("outer function")

# outer()

# first example......

# def decorator_function(func):

#     def wrapper():
#         print("Before function")
#         func()
#         print("after function")

#     return wrapper

# # decorator apply

# @decorator_function

# def greet():
#     print("hey beti pushpa")

# greet()

# decorator with argument ......

def decorator_function(func):

    def wrapper(*args):
        print("Before function")
        func(*args)
        print("after function")

    return wrapper

# decorator apply

@decorator_function

def greet(*args):
    print("hey beti pushpa",*args)

greet(" KE HAAL HEIN","hii mohit")

## MULTIPLE DECORATORS>>>>>>

# def star(func):

#     def wrapper():
#         print("******")
#         func()
#         print("******")

#     return wrapper

# def hash(func):

#     def wrapper():
#         print("#######")
#         func()
#         print("#######")

#     return wrapper



# # decorator apply

# @star
# @hash
# def greet():
#     print("hey beti pushpa",)

# greet()