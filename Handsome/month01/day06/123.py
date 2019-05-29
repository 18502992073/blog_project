dict = {'Name': 'Runoob', 'Age': 7}
print("Value : %s" % dict.items())


d01 = {}
d01 = {"zs":18,"ls":28}
d01["wz"] = 20
d01["qtx"] = 16
d01["dd"] = 20
for key in d01:
    print(key)

# 遍历字典记录(键值对)
for item in d01.items():
    # item 是元组
    print(item)#[0],item[1])

# for value in d01.values():
#     print(value)
#
# print(d01)
