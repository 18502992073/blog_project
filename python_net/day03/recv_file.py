from socket import *

s = socket()
s.bind(('127.0.0.1', 12345))
s.listen(3)

c, addr = s.accept()
print("connect from", addr)

f = open('99.txt', 'w')

while True:
    data = c.recv(1024)
    if not data:
        break
    f.write(data.decode())

f.close()
c.close()
s.close()