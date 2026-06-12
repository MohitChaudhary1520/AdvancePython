# try:
#     num = int(input("enter a number : "))
#     result = 100/num
#     print(result)

# except Exception as e:
#     print(e)

# except Exception as e:
#     print(e)

# finally:
#     print("always executed")

class InvalidAgeError(Exception):  # user defined exception
    pass

try:
    age = int(input("enter age : "))

    if age < 0 :
        raise InvalidAgeError("Age cannot be nagative") # we can create our own exception
    
    print("Age: " , age)

except InvalidAgeError as e:   # exception as object
    print(e)