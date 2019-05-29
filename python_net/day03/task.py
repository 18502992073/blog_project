import sys
from select import *
from socket import *
from time import *

"""
    将从客户端发来信息写入到一个文件日志中，同时服务端接收终端输入内容，也写入到该日志中。
"""

# 创建套接字作为关注的IO
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(('0.0.0.0', 12345))
sockfd.listen(5)

# 创建要关注的IO
st = sys.stdin

# 关注IO
rlist = [sockfd, st]
wlist = []
xlist = []

# 打开日志文件
f = open("log.txt", "a")

# 记录日志
while True:
    rs, ws, xs = select(rlist, wlist, xlist)
    for r in rs:
        if r is sockfd:
            connfd, addr = r.accept()
            rlist.append(connfd)
            t = strftime("%Y-%m-%d %H:%M:%S ", localtime())
            f.write(t + "connect from %s \r\n" % str(addr))
            f.flush()
        elif r is st:
            t = strftime("%Y-%m-%d %H:%M:%S ", localtime())
            f.write(t + "server:" + r.readline())
            f.flush()
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            t = strftime("%Y-%m-%d %H:%M:%S ", localtime())
            f.write("%s %s: %s \r\n" % (t, data.decode(), str(r.getpeername())))
            f.flush()
            wlist.append(r)
    for w in ws:
        w.send(b'ok')
        wlist.remove(w)
    for x in xs:
        pass
