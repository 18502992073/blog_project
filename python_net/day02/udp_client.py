from socket import *

# 服务端地址
HOST = "127.0.0.1"
PORT = 12345
ADDR = (HOST, PORT)

# 创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 收发消息
while True:
    data = input(">>")
    if not data:
        break
    sockfd.sendto(data.encode(), ADDR)
    msg, addr = sockfd.recvfrom(1024)
    print("from server:", msg.decode())

sockfd.close()
