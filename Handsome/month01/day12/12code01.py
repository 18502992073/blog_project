class Person:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value


class Bank:
    def __init__(self, name, total_money):
        self.name = name
        self.total_money = total_money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def total_money(self):
        return self.__total_money

    @total_money.setter
    def total_money(self, value):
        self.__total_money = value

    def draw_money(self, quantity, person):
        person.money += quantity
        self.total_money -= quantity


xm = Person("小明", 0)
bank = Bank("招商银行", 10000)
zs.draw_money(1000, xm)
print(xm.money)
print(zs.total_money)
