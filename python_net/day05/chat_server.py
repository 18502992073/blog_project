# -*- coding:utf-8 -*-
"""
    Chat room server
    evn:python3.5
    exc:for socket and fork
"""

from socket import *
import os, sys

# 服务端地址
ADDR = ('0.0.0.0', 12345)
# 存储用户
user = {}


# 搭建网络连接
def udp_server():
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(ADDR)
    print("服务器已启动")
    return s


def do_login(s, name, addr):
    if (name in user) or ("管理员" in name):
        s.sendto("该用户已存在".encode(), addr)
        return
    s.sendto(b'OK', addr)

    # 通知其他人
    msg = "\n 欢迎 %s 进入聊天室" % name
    for i in user:
        s.sendto(msg.encode(), user[i])
    # 加入字典
    user[name] = addr


def do_transpond(s, name, text):
    msg = "\n%s:%s" % (name, text)
    for i in user:
        if i != name:
            s.sendto(msg.encode(), user[i])


def do_user_exit(s, name):
    s.sendto(b"EXIT", user[name])
    del user[name]  # 删除用户
    msg = "\n用户%s退出聊天室" % name
    for i in user:
        s.sendto(msg.encode(), user[i])


def request(s):
    while True:
        data, addr = s.recvfrom(1024)
        msgList = data.decode().split(" ")
        # 区分请求类型
        if msgList[0] == "L":   # L登录请求
            do_login(s, msgList[1], addr)
        elif msgList[0] == "X": # X聊天请求
            # 重组消息
            text = " ".join(msgList[2:])
            do_transpond(s, msgList[1], text)
        elif msgList[0] == "Q": # Q退出请求
            do_user_exit(s, msgList[1])


def main():
    s = udp_server()
    # 单独创建进程发送管理员消息
    pid = os.fork()
    if pid < 0:
        print("Error")
    elif pid == 0:
        while True:
            msg = input("管理员消息：")
            msg = "X 管理员消息 " + msg
            # 发送给父进程
            s.sendto(msg.encode(), ADDR)
    else:
        request(s)  # 接收请求
main()