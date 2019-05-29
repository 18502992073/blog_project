from select import *
from socket import *

f = open('test.jpg')
s = socket()
s.bind(('127.0.0.1', 12345))
s.listen(3)

print("监控IO")
rs, ws, xs = select([s], [], [f])
print(rs)
print(ws)
print(xs)
