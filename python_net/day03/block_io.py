from socket import *
from time import *

# 创建tcp套接字
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(('127.0.0.1', 12345))
sockfd.listen(3)

# 设置非阻塞状态
# sockfd.setblocking(False)

# 设置阻塞时间
sockfd.settimeout(3)

while True:
    print("waiting for connect")
    try:
        connfd, addr = sockfd.accept()
    except BlockingIOError:
        sleep(2)
        print("%s connect error" % ctime())
        continue
    except timeout:
        print("timeout...")
    else:
        print("connect from", addr)
        data = connfd.recv(1024)
