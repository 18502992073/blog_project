import struct
from socket import *


fmt = 'i32sif'
ADDR = ('127.0.0.1', 12345)
s = socket(AF_INET, SOCK_DGRAM)

while True:
    id = int(input("id:"))
    name = input("name:")
    age = int(input("age:"))
    score = float(input("score:"))

    data = struct.pack(fmt, id, name.encode(), age, score)
    s.sendto(data, ADDR)
s.close()

