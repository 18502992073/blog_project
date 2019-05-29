import sys
import time
from socket import *

ADDR = ("127.0.0.1", 12345)


class FtpClient:
    def __init__(self, sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b"L")  # 发送请求
        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == "OK":
            files = self.sockfd.recv(4096).decode()

            for file in files.split('#'):
                print(file)
        else:
            # 无法完成操作
            print(data)

    def do_quit(self):
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit("谢谢使用")

    def do_download(self, file_name):
        self.sockfd.send(("D " + file_name).encode())
        data = self.sockfd.recv(128).decode()
        if data == "OK":
            fd = open(file_name, "wb")
            while True:
                data = self.sockfd.recv(1024)
                if data == b'##':
                    break
                fd.write(data)
            fd.close()
        else:
            print(data)

    def do_upload(self, file_name):
        try:
            f = open(file_name, "rb")
        except Exception:
            print("读取文件错误")
            return
        filename = file_name.split("/")[-1]
        self.sockfd.send(("U " + filename).encode())
        data = self.sockfd.recv(128).decode()
        if data == "Exist":
            self.sockfd.send(input("文件已存在是否覆盖它?[Y/N]").encode())
        data = self.sockfd.recv(128).decode()
        if data == "OK":
            while True:
                data = f.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.sockfd.send(b"##")
                    break
                self.sockfd.send(data)
            f.close()
        else:
            print(data)


def main():
    # 创建套接字
    sockfd = socket()
    try:
        sockfd.connect(ADDR)  # 发起连接
    except Exception as e:
        print(e)
        return
    # 创建对象
    ftp = FtpClient(sockfd)
    # 收发消息
    while True:
        print("""
*************
1.查看文件列表
2.上传文件
3.下载文件
4.退出
*************
""")
        cmd = input("输入命令")
        if cmd == "1":
            ftp.do_list()
        elif cmd == "2":
            file_name = input("请输入带完整路径的文件名：")
            ftp.do_upload(file_name)
        elif cmd == "3":
            file_name = input("请输入文件名：")
            ftp.do_download(file_name)
        elif cmd == "4":
            ftp.do_quit()
        else:
            print("无效命令！")


if __name__ == "__main__":
    main()
