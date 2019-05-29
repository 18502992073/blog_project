from socket import *

s = socket()
s.connect(('127.0.0.1', 12345))

f = open('11.txt', 'r')

while True:
    data = f.readline()
    if not data:
        break
    s.send(data.encode())

f.close()
s.close()