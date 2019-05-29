from socket import *
from struct import *

import pymysql

db = pymysql.connect('localhost', 'root', '123456', 'eshop', charset="utf8")
cursor = db.cursor()

s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 12345))

st = Struct('i32sif')

while True:
    data, addr = s.recvfrom(1024)
    data = st.unpack(data)
    id = data[0]
    name = data[1].decode()
    age = data[2]
    score = data[3]
    sql = "insert into stu values(%d,'%s',%d,%f)" % (id, name, age, score)
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print("Error:", e)
        db.rollback()
s.close()
db.close()
