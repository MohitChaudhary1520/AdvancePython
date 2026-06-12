# FIRST NORMAL PROCESS CODE>>>>>>

# from multiprocessing import Process

# def task():
#     print("pushpa is running....")

# if __name__ == '__main__':

#     p =Process(target=task)

#     p.start()
#     p.join()
   
#     print("heyyy hemant")

#PROCESS ID each process has unique id......

# from multiprocessing import Process
# import os

# def task():

#     print("Pushpa id :" ,os.getpid())

# print("Hemant id : ", os.getpid())


# if __name__ == '__main__':

#     p = Process(target=task)

#     p.start()
#     p.join()
   
#     print("heyyy hemant")

# CREATING MULTIPLE PROCESS>>>>>

# from multiprocessing import Process
# import os

# def task():
#     print("Pushpa running")

# if __name__ == '__main__':

#     for i in range(5):
#         p = Process(target=task())

#     p.start()
#     p.join()

#     print("STOP pushpa you done great job")

# PASSING ARGUMENT>>>>

# from multiprocessing import Process
# import os

# def task(name):
#     print("Pushpa running",name)

# if __name__ == '__main__':

    
#     p = Process(target=task, args=("mohit",))

#     p.start()
#     p.join()

#     print("STOP pushpa you done great job")

# MULTIPE ARGUMENT>>>

# from multiprocessing import Process
# import os

# def task(a,b):
#     print (a+b)
    
# if __name__ == '__main__':

    
#     p = Process(target=task, args=(10,20))

#     p.start()
#     p.join()

#     print("STOP pushpa you done great job")

# PARALLEL EXECUTION OF MULTIPLE PROCESS COMPARIION WITH TIME>>>

# from multiprocessing import Process
# from time import time

# def work():
#     for i in range(10000000):
#         pass

# if __name__ == '__main__':

#     processes = []
#     start = time()

#     for i in range(4):
#         p = Process(target=work)
#         p.start()
#         processes.append(p)
   
#     for p in processes:
#         p.join()

#     end = time()
#     print(f"TOtal time for execution: {end-start: .2f} seconds")

# IPC -- INTER PROCESS COMMUNICATION USE TO COMMUNICATE BETWEEN PROCESSES...

# QUEUE... MOST COMMON IPC machanism.....

# from multiprocessing import Process, Queue

# def square(num,q):
#     q.put(num*num)

# if __name__ == "__main__":
#     q = Queue()

#     p = Process(target=square, args= (5,q))

#     p.start()
#     p.join()
#     print(q.get())

# PROCESS POOl creating 100 of process manualyy is inefficient that's why we use pool.....

# from multiprocessing import Pool

# def square(n):
#     return n*n

# if __name__ == '__main__':
#     with Pool() as pool:
#         result = pool.map(square,[1,2,3,4,5,6,7])

#     print(result)

# CPU COUNT>>>

# import multiprocessing

# print(multiprocessing.cpu_count())

# DOWNLAOD SIMULATION>>>>

from multiprocessing import Pool
import time

def download(file):
    time.sleep(2.0)
    return f"{file} done"

if __name__ == '__main__':
    files =[ "image.jpg","files.png","files.pdf"]

    with Pool() as pool:
        result = pool.map(download,files)

    print(result)
