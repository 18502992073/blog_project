from pymongo import MongoClient

conn = MongoClient('localhost', 27017)
db = conn.images
myset = db.girl

# 存储图片
# with open('test.jpg', 'rb') as f:
#     data = f.read()

# 将data转换为bson格式
# content = bson.binary.Binary(data)

# 插入到集合
# dic = {'filename': 'girl.jpg', 'data': content}
# myset.insert_one(dic)

# 提取文件
img = myset.find_one({'filename': 'girl.jpg'})
with open('0.jpg', 'wb') as f:
    print(img)
    f.write(img['data'])

conn.close()
