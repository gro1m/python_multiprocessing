import random
import time
import collections
import cProfile
from multiprocessing  import Process

LIST_LEN = 14000

def timefunc(f):
    t = time.time()
    f()
    return time.time() - t

NUM_RANGE = 100000000

def multi():
    class MultiProcess(Process):
        def __init__(self):
            Process.__init__(self)

        def run(self):
            # Alter string + test processing speed
            for i in range(1,NUM_RANGE):
                a = 20 * 20

    thread1 = MultiProcess()
    thread2 = MultiProcess()
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

def single():
    for i in range(1, NUM_RANGE):
        a = 20 * 20

    for i in range(1, NUM_RANGE):
        a = 20 * 20

print(timefunc(multi) / timefunc(single))
