from socket import *

# 创建套接字
s = socket()

# 发起连接
sever_addr = ("127.0.0.1", 12345)
s.connect(sever_addr)

# 收发消息

while 1:
    data = input(">>")
    if not data:
        break
    s.send(data.encode())
    data = s.recv(1024)
    print("from server:", data.decode())

# 关闭套接字
s.close()
