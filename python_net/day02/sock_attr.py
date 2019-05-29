"""
    套接字属性演示
"""
from socket import *

s = socket()
print(s.family)  # 地址类型
print(s.type)  # 套接字类型
print(s.getsockname())  # 绑定地址
print(s.fileno())   # 文件描述符

# s.listen(5)
# c,addr=s.accept()
# print(c.getpeername())  # 连接套接字客户端地址


