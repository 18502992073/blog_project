class Player:
    def __init__(self, name, atk, blood=0):
        self.name = name
        self.atk = atk
        self.blood = blood

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        self.__atk = value

    @property
    def blood(self):
        return self.__blood

    @blood.setter
    def blood(self, value):
        self.__blood = value

    def attack(self, enemy):
        print("玩家攻击敌人啦")
        enemy.damage(self.atk)


    def damage(self, value):
        self.blood -= value
        print("碎屏")
        if self.__blood<=0:
            self.__death()

    def __death(self):
        print("game over")


class Enemy:
    def __init__(self, name, atk, blood=0):
        self.name = name
        self.atk = atk
        self.blood = blood

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        self.__atk = value

    @property
    def blood(self):
        return self.__blood

    @blood.setter
    def blood(self, value):
        self.__blood = value

    def attack(self, player):
        print("敌人攻击玩家啦")
        player.damage(self.atk)

    def damage(self, value):
        print("敌人受伤啦")
        self.__blood -=value
        if self.blood<=0:
            self.__death()

    def __death(self):
        print("敌人死亡！")

p01 = Player("zs",50,100)
e01 = Enemy("rt",5,50)
e01.attack(p01)
p01.attack(e01)




