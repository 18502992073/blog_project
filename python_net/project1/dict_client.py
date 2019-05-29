import sys
import getpass
from socket import *

HOST = '176.234.2.27'
PORT = 12345
ADDR = (HOST, PORT)
s = socket()
try:
    s.connect(ADDR)
except Exception as e:
    print(e)
    sys.exit()


# 创建网络连接
def main():
    while True:
        print("""
        ============Welcome===========
        --1.注册      2.登录    3.退出--
        ==============================""")
        cmd = input("输入选项：")
        if cmd not in ['1', '2', '3']:
            print("请输入正确选项")
        elif cmd == '1':
            do_register()
        elif cmd == '2':
            do_login()
        elif cmd == "3":
            s.send(b"E")
            sys.exit("谢谢使用")


def do_register():
    while True:
        name = input("请输入昵称")
        passwd = getpass.getpass("请输入密码")
        passwd2 = getpass.getpass("请确认密码")
        if (' ' in name) or (' ' in passwd):
            print("用户名密码不能有空格")
            continue
        if passwd != passwd2:
            print("两次密码不一致")
            continue
        msg = "R %s %s" % (name, passwd)
        # 发送请求
        s.send(msg.encode())
        # 等待回复
        data = s.recv(128).decode()
        if data == "OK":
            print("注册成功")
            login(name)
        else:
            print(data)
        return


def do_login():
    while True:
        name = input("请输入用户名")
        passwd = getpass.getpass("请输入密码")
        msg = "L %s %s" % (name, passwd)
        # 发送请求
        s.send(msg.encode())
        # 等待回复
        data = s.recv(128).decode()
        if data == "OK":
            print("登录成功")
            login(name)
        else:
            print(data)
        return


# 二级界面
def login(name):
    while True:
        print("""
        =============QUERY============
        --1.查询   2.历史记录    3.注销--
        ==============================""")
        cmd = input("输入选项：")
        if cmd not in ['1', '2', '3']:
            print("请输入正确选项")
        elif cmd == '1':
            do_query(name)
        elif cmd == '2':
            do_history(name)
        elif cmd == "3":
            return


def do_query(name):
    while True:
        word = input("请输入单词：")
        if word == "##":
            return
        msg = "Q %s %s" % (name, word)
        s.send(msg.encode())
        data = s.recv(2048).decode()
        print(data)


def do_history(name):
    msg = "H %s" % name
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data == "OK":
        while True:
            data = s.recv(2048).decode()
            if data == "##":
                break
            print(data)
    else:
        print(data)

main()
