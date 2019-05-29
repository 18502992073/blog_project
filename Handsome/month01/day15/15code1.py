"""
class Pet:
    def __init__(self,name):
        self.name=name

class Dog(Pet):
    def __init__(self,name,work):
        super().__init__(name)
        self.work=work

class Cat(Pet):
    def catch(self):
        print("爪")
pet1=Pet("11")
dog1=Dog("hh","ww")
print(dog1.name,dog1.work)
cat1=Cat("cc")
cat1.catch()
print(cat1.name)
print(isinstance(dog1,Dog),isinstance(dog1,Pet),isinstance(dog1,Cat))
print(isinstance(cat1,Cat),isinstance(cat1,Pet),isinstance(cat1,Dog))
"""
class GraphicManage:
    def __init__(self):
        self.graphic=[]
    def get_total_area(self):
        sum=0
        for item in self.graphic:
            sum +=item.calculate_area()
        return sum

class Graphic:
    def __init__(self,name):
        self.name=name
    def calculate_area(self):
        raise NotImplementedError()

class Circle(Graphic):
    def __init__(self,name,R):
        super().__init__(name)
        self.r=R

    def calculate_area(self):
        return 3.14*self.r**2

class Rectangle(Graphic):
    def __init__(self,name,a,b):
        super().__init__(name)
        self.a=a
        self.b=b
    def calculate_area(self):
        return self.a*self.b

manager=GraphicManage()
cir1=Circle("圆1",10)
manager.graphic.append(cir1)
cir2=Circle("圆2",10)
manager.graphic.append(cir2)
rec1=Rectangle("矩形1",10,10)
manager.graphic.append(rec1)
print(manager.get_total_area())











