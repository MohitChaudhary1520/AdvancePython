
# CREATING THREAD>>>>>>>
# from threading import Thread

# class Hello(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hello ", i+1)

# class Hi(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hi ", i+1)


# t1 = Hello()
# t2 = Hi()

# t1.start()
# t2.start()

# BY USING SLEEP WE CAN TRY FOR FUNC RUN SIMULTANEUSLY>>>>>>>>

# from threading import Thread
# from time import sleep

# class Hello(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hello ", i+1)
#             sleep(0.3)

# class Hi(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hi ", i+1)
#             sleep(0.3)


# t1 = Hello()
# sleep(0.1)
# t2 = Hi()

# t1.start()
# t2.start()


# USING FUNCTION>>>>>>>

# from threading import Thread
# from time import sleep

# def hello():
#     for i in range(5):
#         print("Hello ", i+1)
#         sleep(0.3)


# def hi():
#     for i in range(5):
#         print("Hi ", i+1)
#         sleep(0.3)


# t1 = Thread(target=hello)
# sleep(0.1)
# t2 = Thread(target=hi)

# t1.start()
# t2.start()
# t1.join() #we using join for wait until i fineshed work then do any other work like print byeee thats why byeee prnt at the end.....
# t2.join()

# print("byeeeee")

# USING ANOTHER EXAMPLE FOR SPEED HOW ITS WORK>>>>>>

# from threading import Thread
# from time import sleep, time

# def download(file_name):
#     print("DOWNLOADING FILE.....", file_name)
#     sleep(0.5)
#     print("DOWNLOAD COMPLETE>")

# files=["image.jpg","files.png","file.pdf"]

# start =time()
# for f in files:
#     download(f)
# end = time()
# print(f"Serial time {end - start: .2f} seconds")

# threads=[]

# for f in files:
#     t = Thread(target=download, args = (f,))
#     threads.append(t)

# start = time()

# for t in threads:
#     t.start()

# for t in threads:
#     t.join()

# end = time()
# print(f"parallell with threads time {end - start: .2f} seconds")

# print("byeeeee")

# HOW GIL WORK AND THE SOLUTION IS PROCESS INSTEAD OF THREAD>>>>>>>>>

from threading import Thread
from time import sleep, time
from multiprocessing import Process

def calculate(n1,n2):
    sum = 0
    for n in range(n1,n2):
        sum += n*n

if __name__ == '__main__':
    num = 50_000_000

    start =time()

    calculate(0,num)

    end = time()

    print(f"Serial time {end - start: .2f} seconds")

    mid = num//2

    t1 = Thread(target=calculate,args = (0,mid))
    t2 = Thread(target=calculate,args= (mid,num))

    start = time()

    t1.start()
    t2.start()
    t1.join()
    t2.join()


    end = time()

    print(f"parallell with threads time {end - start: .2f} seconds")

    t1 = Process(target=calculate,args = (0,mid)) 
    t2 = Process(target=calculate,args= (mid,num))

    start = time()

    t1.start()
    t2.start()
    t1.join()
    t2.join()


    end = time()
    print(f"parallell with process time {end - start: .2f} seconds")

    print("byeeeee")
