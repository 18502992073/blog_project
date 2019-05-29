import pymysql
import re

conn = pymysql.connect('localhost', 'root', '123456', 'dict')
cursor = conn.cursor()
f = open('dict.txt')
for line in f:
    word_list = line.split(' ')
    word = word_list[0]
    word_explain = ' '.join(word_list[1:]).strip()
    sql = 'INSERT into words (word, mean) VALUES ("%s", "%s");'%(word, word_explain)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
cursor.close()
f.close()



