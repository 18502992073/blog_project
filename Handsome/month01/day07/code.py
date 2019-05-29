list1 = ["zs", "wlw", "tarena"]
dic = {i: len(i) for i in list1}
print(dic)

list1 = [101, 102, 103]
list2 = ["zs", "ls", "ww"]
dt = {}

dic = {list1[i]: list2[i] for i in range(len(list1))}
print(dic)

set1 = set()
i = 0
while True:
    str_input = input("请输入：")
    if str_input != "":
        i += 1
        set1.add(str_input)
    else:
        break
print("总共输入%d次" % (i))
for i in set1:
    print(i, end=" ")


list01 = ["曹操", "刘备", "孙权"]
list02 = ["曹操", "刘备", "张飞", "关羽"]
set01 = set(list01)
set02 = set(list02)
print("既是经理又是技术员的有:",set01 & set02)
print("是经理,但不是技术员的有:",set02-set01)
print("是技术员,但不是经理的有:",set01-set02)
print("张飞是经理吗？","张飞" in set01)
print("身兼一职：",set01^set02)
print("经理和技术员共有:%d人"%len(set01|set02))

