from multiprocessing import Process
from threading import Thread
from time import *

from python_net.day07.test import *

t0 = time()
for i in range(10):
    io()
print(time() - t0)


t1 = time()
process = []
for j in range(10):
    p = Process(target=io)
    process.append(p)
    p.start()

for p in process:
    p.join()

print(time() - t1)


t2 = time()
thr = []
for k in range(10):
    t = Thread(target=io)
    thr.append(t)
    t.start()

for t in thr:
    t.join()

print(time() - t2)
