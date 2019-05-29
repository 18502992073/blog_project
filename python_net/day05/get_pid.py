import os
from time import sleep

pid = os.fork()

if pid < 0:
    print("error")
elif pid == 0:
    sleep(0.5)
    print("child pid", os.getpid())
    print("get parent pid", os.getppid())
else:
    print("parent pid", os.getpid())
    print("get child pid", pid)
