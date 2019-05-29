R = int(input("输入圆的半径："))
PI = 3.14
area = PI * R ** 2
length = 2 * PI * R
print("圆的面积是：" + str(area) + "，圆的周长是：" + str(length) + "．")
print("圆的面积是：{}，圆的周长是：{:.1f} ．".format(area,length))