# iterator.........

# my_list = [10,20,30,40,50]

# it = iter(my_list)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# creating custom iterator.......

class Numbers:
    def __init__(self):
        self.num =1

    def __iter__(self):
        return self
    
    def __next__(self):

        if self.num <= 5:
            val = self.num
            self.num += 1
            return val
        
        else:
            raise StopIteration
        
obj = Numbers()
it = iter(obj)

print(next(it))



for i in obj:    # loop can not repeat iter value  in loop.........
    print(i)