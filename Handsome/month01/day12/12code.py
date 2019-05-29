class Student:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


stu1 = Student("ytt", 0)
stu1.set_name("sdad")
print(stu1.get_name())


class Student:
    def __init__(self, name, age, score, sex):
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, value):
        self.__sex = value


stu = Student("wang", 60, 90, "nan")
stu.age = 20
stu.score = 100
print(stu.name, stu.age, stu.sex, stu.score)
