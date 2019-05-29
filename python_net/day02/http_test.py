from socket import *

s = socket()
s.bind(("0.0.0.0",12345))
s.listen(5)

c,addr = s.accept()
print("连接地址",addr)
data = c.recv(4096)
print(data)

data = """HTTP/1.1 200 OK
Content - Type: text/html
hello world

"""

c.send(data.encode())

c.close()
s.close()