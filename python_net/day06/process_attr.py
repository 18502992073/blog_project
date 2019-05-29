from multiprocessing import *
from time import *


def fun():
    for i in range(3):
        sleep(2)
        print(ctime())


p = Process(target=fun)
p.daemon = True
p.start()
print("Name:", p.name)
print("PID:", p.pid)
print("alive:", p.is_alive())
