class Person:
    def go_home(self, vehicle):
        vehicle.transport()

# class Vehicle:
#     """
#         交通工具
#     """
#     def transport(self):
#         raise NotImplementedError()


class Train:
    """
        火车类
    """
    def transport(self):
        print("呜呜呜~")


class Airplane:
    """
        飞机类
    """
    def transport(self):
        print("嗖嗖~")


class Car:
    """
        汽车类
    """
    def transport(self):
        print("滴滴呜呜~")


# 测试..............................
p01 = Person()
p01.go_home(Train())
p01.go_home(Airplane())
p01.go_home(Car())


