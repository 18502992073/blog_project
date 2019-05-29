class Wife01():
    def __init__(self, name, age, sex):
        Wife01.name = name
        Wife01.age = age
        Wife01.sex = sex

    def cooking(self):
        print("做饭")


w01 = Wife01("铁锤", 20, "男")
w01.cooking()
w02 = Wife01("如花", 36, "女")
w02.cooking()
w01.cooking()


class Car():
    def __init__(self, type, speed):
        Car.type = type
        Car.speed = speed

    def start(self):
        print("start")

    def stop(self):
        print("stop")

    def run(self):
        print("run")


car01 = Car("宝马", 80)
car02 = Car("比亚迪", 75)
car01.stop()
