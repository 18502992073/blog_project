"""
 作业2：定义技能数据类(技能编号，技能名称，消耗法力，冷却时间，动画名称)，使用属性进行封装，使用__slots__。
"""


class Skill:
    __slots__ = ("__number", "__skill_name", "__cost_SP", "__cool_time", "__motion_name")

    def __init__(self, number, skill_name, cost_SP, cool_time, motion_name):
        self.number = number
        self.skill_name = skill_name
        self.cost_SP = cost_SP
        self.cool_time = cool_time
        self.motion_name = motion_name

    @property
    def motion_name(self):
        return self.__motion_name

    @motion_name.setter
    def motion_name(self, value):
        self.__motion_name = value

    @property
    def cooling_time(self):
        return self.__cooling_time

    @cooling_time.setter
    def cooling_time(self, value):
        self.__cooling_time = value

    @property
    def consume_power(self):
        return self.__consume_power

    @consume_power.setter
    def consume_power(self, value):
        self.__consume_power = value

    @property
    def skill_name(self):
        return self.__skill_name

    @skill_name.setter
    def skill_name(self, value):
        self.__skill_name = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value


# fdd = Skill(0, "降龙", 50, 2, "飞龙在天")

"""
扩展作业3：使用代码描述一下场景
张三 教 李四 学王者荣耀。
李四 教 张三 学Python
李四 上班赚了 5000元钱
最后输出张三具有的技能，李四具有的技能，以及他们的钱。
"""


class Person:
    def __init__(self, name, money=0):
        self.name = name
        self.skill = []
        self.money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def skill(self):
        return self.__skill

    @skill.setter
    def skill(self, value):
        self.__skill=value

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value

    def teach(self, person_other, skill):
        person_other.__skill.append(skill)
        print("%s教%s%s" % (self.name, person_other.name, skill))

    def working(self, who, salary):
        who.money += salary


zs = Person("张三")
zs.skill.append("python")
ls = Person("李四")
ls.skill.append("王者")
zs.teach(ls, "python")
ls.teach(zs, "王者")
ls.working(ls, 5000)
print(zs.skill)
print(ls.skill)
print(ls.money)
