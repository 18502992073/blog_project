total = int(input("输入总秒数："))
hour = total // 3600
minute = total % 3600 // 60
second = total - hour * 3600 - minute * 60
print("总时间为：" + str(hour) + "小时" + str(minute) + "分钟" + str(second) + "秒")
