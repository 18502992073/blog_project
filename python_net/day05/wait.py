import os
from time import sleep

pid = os.fork()

if pid < 0:
    print("error")
elif pid == 0:
    sleep(3)
    print("child %d process exit" % os.getpid())
    os._exit(2)
else:
    pid, status = os.wait()
    print("pid", pid)
    print("status", status)
    while True:
        sleep(100)
