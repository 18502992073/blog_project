from socket import *

# 创建套接字
sockfd = socket(AF_INET, SOCK_STREAM)
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,True)

# 绑定地址
sockfd.bind(("0.0.0.0", 12345))

# 设置监听
sockfd.listen(3)

# 等待客户端连接
while True:
    print("waitting for connect....")
    try:
        connfd, addr = sockfd.accept()
    except KeyboardInterrupt:
        print("server exit")
        break
    print("connect from", addr)  # 打印客户端地址

# 收发消息
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print("receive message:", data.decode())
        n = connfd.send(b"recevie you message")
        print("send %d bytes" % n)
    connfd.close()

# 关闭套接字
sockfd.close()
