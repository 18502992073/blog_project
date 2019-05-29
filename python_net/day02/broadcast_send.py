from socket import *
from time import sleep



#目标地址
addr = ("176.234.2.255",12345)


s = socket(AF_INET,SOCK_DGRAM)

# 设置可以发送接收广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,True)

data = """
*******************
    4.4清明节
    借问酒家何处有
    牧童遥指杏花村
*******************
"""
while True:
    sleep(0.5)
    s.sendto(data.encode(), addr)