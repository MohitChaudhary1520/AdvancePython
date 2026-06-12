# using with statement as context manager....

# with open("newfile.txt","r") as file:
#     data = file.read()
#     print(data)

# using __enter__ and __exit__  method in context manager.....

class Mycontext:
    def __enter__(self):
        print("enter context")
        return self
    
    def __exit__(self, exc_type, exc, tb):
        print("exit context")

with Mycontext():
    print("inside function")