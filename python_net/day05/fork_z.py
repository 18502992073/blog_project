import os
from time import *

pid = os.fork()

if pid == 0:
    print("child process:",os.getpid())
    os._exit(0)
else:
    print("parent process,长点心吧..")
    while True:
        pass
