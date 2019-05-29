"""
    http server 1.0
    接收浏览器请求
    将固定的网页发送给浏览器
"""
from socket import *


# 处理客户请求
def handle_request(connfd):
    print("request from:", connfd.getpeername())
    request = connfd.recv(4096)  # 接收请求
    print(request)

    # 获取请求行
    request_lines = request.splitlines()
    for line in request_lines:
        print(line)

    # 返回固定网页给浏览器
    try:
        f = open('index.html')
    except IOError:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += '\r\n'
        response += '==Sorry not found=='
    else:
        response = "HTTP/1.1 200 OK \r\n"
        response += '\r\n'
        response += f.read()
        f.close()
    finally:
        connfd.send(response.encode())


# 创建套接字
def main():
    sockdf = socket()
    sockdf.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockdf.bind(('0.0.0.0', 12345))
    sockdf.listen(3)
    print("listen the port 12345...")
    while True:
        connfd, addr = sockdf.accept()
        handle_request(connfd)  # 具体请求处理
        connfd.close()


if __name__ == "__main__":
    main()
