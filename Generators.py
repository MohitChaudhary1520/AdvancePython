# def generator():
#     yield 1
#     yield 2
#     yield 3

# print(next(generator()))

# def numbers(n):
#     for i in range(1,n):
#         yield i
        

# gen = numbers(100)

# for i in gen:
#     print(i)

# def count():
#     for i in range(1, 6):
#         yield i

# for num in count():
#     print(num)

## genertor expression......... [] used by list comprhension and () used by generator expression.......

# list comprehension....

# nums = [x*x for x in range (5)]
# print(nums)

# generator expression

# nums = ( x*x for x in range(5))
# print(next(nums))
# print(next(nums))
# print(next(nums))

## fibonacci generator ........

def Fibonacci(n):
    a,b = 0,1

    for i in range(n):
        yield a
        a,b = b,a+b

for num in Fibonacci(7):
    print(num)