class Car:
    def __init__(self,type="",speed=0,weight=0):
        self.type=type
        self.speed=speed
        self.weight=weight
    def print_info(self):
        print(self.type,self.speed,self.weight)


list_cars=[]
while True:
    car=Car()
    car.type=input("请输入车型：")
    if car.type=="e":
        break
    car.speed=int(input("请输入速度："))
    car.weight=int(input("请输入重量："))
    list_cars.append(car)
for i in list_cars:
    i.print_info()