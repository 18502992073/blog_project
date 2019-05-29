import os
import sys
from socket import *

# 服务器地址
ADDR = ('127.0.0.1', 12345)


def udp_clinet():
    return socket(AF_INET, SOCK_DGRAM)


def login(s):
    while True:
        name = input("请输入姓名:")
        msg = "L " + name  # L表示请求类型
        # 给服务器发送
        s.sendto(msg.encode(), ADDR)
        # 等待回复
        data, addr = s.recvfrom(1024)
        if data.decode() == "OK":
            print("您已进入聊天室")
            break
        else:
            print(data.decode())
    return name


def send_msg(s, name):
    while True:
        try:
            text = input("请输入：")
        except:
            text = "*"
        if text.strip() == "*":
            msg = "Q " + name
            s.sendto(msg.encode(), ADDR)
            sys.exit("退出聊天室")
        else:
            msg = "X %s %s" % (name, text)
            s.sendto(msg.encode(), ADDR)


def recv_msg(s):
    while True:
        data, addr = s.recvfrom(2048)
        if data.decode() == "EXIT":
            sys.exit()
        print(data.decode(), "\n请输入：", end="")


def chat(s, name):
    pid = os.fork()
    if pid == 0:  # 发送消息
        send_msg(s, name)
    elif pid > 0:  # 接收消息
        recv_msg(s)
    else:
        sys.exit("Error")


def main():
    s = udp_clinet()
    name = login(s)
    chat(s, name)


main()
