"""
作业1：在控制台获取季节，返回月份。
key          value
“春”    “1月2月3月”
"""
season = input("请输季节")
dt = {
    "春": "1月2月3月",
    "夏": "4月5月6月",
    "秋": "7月8月9月",
    "冬": "10月11月12月"
}
print(dt[season])

"""
作业2：在控制台中获取一段文字，
打印这个文字中出现的字符以及次数。
“abcaabcd”
a   3
b   2
c   2
d   1
"""
string = input("请输入一段文字：")
dt = {}
for i in string:
    if i not in dt:
        n = string.count(i)
        dt[i] = n
    else:
        continue
for item in dt.items():
    print(item[0], item[1])

d = {}
for ch in string:
    if ch not in d:
        d[ch] = 1
    else:
        d[ch] += 1
for ch, count in d.items():
    print(ch, ":", count, "次")

"""
扩展作业：
游戏：      石头    剪刀   布
在控制台中获取：0    1    2，代表石头剪刀布。
根据游戏规则，显示：平局、胜利、失败。
提示：import  random
      random.randint(0,2)
将胜利策略存入元组((“石头”,”剪刀”),(“剪刀,”布”),(“布”,”石头”))
将用户输入的与系统生成的结果
（"    ”   ，”   ”）in 胜利策略

"""

import random

dt_user = {"石头": 0, "剪刀": 1, "布": 2}
dt_computer = {0: "石头", 1: "剪刀", 2: "布"}
tp_victory = ((0, 1), (1, 2), (2, 0))
tp_dogfall = ((0, 0), (1, 1), (2, 2))
n, m = 0, 0
while n < 2 and m < 2:
    st = input("请输入(石头,剪刀,布)：")  # 0    1    2，代表石头剪刀布
    tp = (dt_user[st], dt_computer[random.randint(0, 2)])
    if tp in tp_victory:
        print("胜利")
        n += 1
    elif tp in tp_dogfall:
        print("平局")
    else:
        print("失败")
        m += 1
    print(st, dt_computer[random.randint(0, 2)])
