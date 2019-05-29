from select import *
from socket import *

# 创建关注的IO
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 12345))
s.listen(5)

# 创建epoll对象
p = epoll()

# 建立地图
fdmap = {s.fileno(): s}

# 关注IO
p.register(s, EPOLLIN | EPOLLERR)

# 循环监控IO
while True:
    events = p.poll()
    # 遍历events处理IO
    for fd, event in events:
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print("connect from", addr)
            # 添加新的关注IO
            p.register(c, EPOLLIN | EPOLLHUP)
            fdmap[c.fileno()] = c
        elif event & EPOLLHUP:
            print("客户端退出")
            p.unregister(fd)
            fdmap[fd].close()
            del fdmap[fd]
        elif event & EPOLLIN:
            data = fdmap[fd].recv(1024)
            print(data.decode())
            fdmap[fd].send(b'ok')
