"""
    使用multiprocessing创建2个子进程，分别复制一个文件的上半部分和下半部分到一个新的文件中
"""
import os
from multiprocessing import *

path = r"test.jpg"
size = os.path.getsize(path)    # 获取文件大小
f = open(path, "rb")


def fun1(path):     # 复制上半部分
    name = path.split(".")
    if name[1] in ("jpg", "jpeg", "bmp", "png", "tif", "gif"):
        with open("file1.%s" % name[1], "wb") as f1:
            f1.write(f.read(size//2))
    elif name[1] in ("txt", "doc", "py"):
        with open("file1.%s" % name[1], "wb") as f1:
            f1.write(f.read(size//2))



def fun2(path):
    f.seek(size//2, 0)
    name = path.split(".")
    if name[1] in ("jpg", "jpeg", "bmp", "png", "tif", "gif"):
        with open("file2.%s" % name[1], "wb") as f2:
            f2.write(f.read())
    elif name[1] in ("txt", "doc", "py"):
        with open("file2.%s" % name[1], "wb") as f2:
            f2.write(f.read())





p1 = Process(target=fun1, args=(path,))
p2 = Process(target=fun2, args=(path,))

p1.start()
p2.start()

p1.join()
p2.join()
f.close()