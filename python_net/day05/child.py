# 二级子进程处理僵尸
import os
from time import sleep


def f1():
    sleep(3)
    print("123")


def f2():
    sleep(4)
    print("456")


pid = os.fork()

if pid < 0:
    print("error")
elif pid == 0:
    p = os.fork()  # 创建二级子进程
    if p == 0:
        f1()
    else:
        os._exit(0)  # 一级子进程退出
else:
    os.wait()  # 回收一级子进程
    f2()
