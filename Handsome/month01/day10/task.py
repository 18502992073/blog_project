"""
作业1：开放性
以“万物皆对象”的思想，审查客观世界中的对象，然后进行抽象化，形成类(数据/行为)。
要求：每个同学自行创建2个类。
"""


class Cup:
    def __init__(self, type, capacity, color):
        self.type = type
        self.capacity = capacity
        self.color = color

    def open(self):
        print("is opening")

    def close(self):
        print("is closed")


cup01 = Cup("玻璃杯", "320ml", "透明")
print(cup01.type)



class Bag:
    def __init__(self,material,color,size):
        self.material=material
        self.color=color
        self.size=size
    def packaging(self):
        print("^_^")
bag1=Bag("纸","白色","中号")
print(bag1.size)
bag1.packaging()
