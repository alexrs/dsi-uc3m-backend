from multiprocessing import Pool, Process
from threading import Thread

import time

def f():
    for i in range(20000000):
        x = i**2

    print(x)

def g(x):
    for i in range(20000000):
        x = i**2

    print(x)


class Calc(Thread):
   def __init__(self):
       Thread.__init__(self)

   def run(self):
       f()


def sequential():
    c = time.time()

    f()
    f()
    f()

    print("Seq", time.time()-c)


def thread_conc():
    c = time.time()

    workers = []

    for i in range(3):
        workers.append(Calc())
        workers[i].start()

    for i in range(3):
        workers[i].join()

    print("thread_conc", time.time()-c)


def pool():
    c = time.time()

    p = Pool(3)
    p.map(g,[1,2,3])

    p.close()
    p.join()

    print("Pool", time.time()-c)


def process():
    c = time.time()


    p1 = Process(target=f)
    p2 = Process(target=f)
    p3 = Process(target=f)


    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()

    print("Process", time.time()-c)


sequential()
thread_conc()
pool()
process()
