"""
    ftp服务器
    fork并发训练
"""
import os
import signal
import sys
import time
from socket import *

# 全局变量
HOST = '0.0.0.0'
PORT = 12345
ADDR = (HOST, PORT)
FILE_PATH = '/home/tarena/test/'


# 服务端功能类
class FtpServer:
    def __init__(self, connfd):
        self.connfd = connfd

    def do_list(self):
        # 获取文件列表
        file_list = os.listdir(FILE_PATH)
        if not file_list:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b"OK")
            time.sleep(0.1)
        files = ""
        for file in file_list:
            if file[0] != '.' and os.path.isfile(FILE_PATH + file):
                files += file + "#"
        self.connfd.send(files.encode())

    def do_download(self, filename):
        try:
            fd = open(FILE_PATH + filename, "rb")
        except IOError:
            self.connfd.send("文件不存在".encode())
            return
        else:
            self.connfd.send(b"OK")
            time.sleep(0.1)
        # 发送文件内容
        while True:
            data = fd.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b"##")
                break
            self.connfd.send(data)
        fd.close()

    def do_upload(self, filename):
        if os.path.exists(FILE_PATH + filename):
            self.connfd.send(b"Exist")
            if self.connfd.recv(128).decode() == "N" or "n":
                self.connfd.send("已退出".encode())
                return
        try:
            fd = open(FILE_PATH + filename, "wb")
        except Exception:
            self.connfd.send("上传文件失败".encode())
            return
        else:
            self.connfd.send(b"OK")
            time.sleep(0.1)
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            fd.write(data)
        fd.close()


# 处理客户端请求
def do_requests(connfd):
    ftp = FtpServer(connfd)
    while True:
        data = connfd.recv(1024).decode()
        if not data or data[0] == "Q":
            connfd.close()
            return
        elif data[0] == "L":
            ftp.do_list()
        elif data[0] == "D":
            filename = data.split(" ")[-1]
            ftp.do_download(filename)
        elif data[0] == "U":
            filename = data.split(" ")[-1]
            ftp.do_upload(filename)


# 网络搭建
def main():
    # 创建套接字
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(ADDR)
    sockfd.listen(5)

    # 处理僵尸进程
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    print("Listen the port 12345...")

    # 循环等待客户端连接
    while True:
        try:
            conntfd, addr = sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit("服务器退出")
        except Exception:
            continue
        print("Connect from", addr)

        # 创建子进程
        pid = os.fork()

        if pid == 0:
            sockfd.close()
            do_requests(conntfd)  # 处理客户端请求
            os._exit(0)
        else:
            conntfd.close()


if __name__ == "__main__":
    main()
