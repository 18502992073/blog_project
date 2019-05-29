class ImpactEffect:
    """
        影响效果
    """

    def impact(self):
        raise NotImplementedError()


class CostSpEffect(ImpactEffect):
    """
        消耗法力
    """

    def __init__(self, value):
        self.value = value

    def impact(self):
        print("消耗%s法力" % self.value)


class DamagedEffect(ImpactEffect):
    """
        伤害生命
    """

    def __init__(self, value):
        self.value = value

    def impact(self):
        print("伤害%s生命" % self.value)


class LowerSpeedEffect(ImpactEffect):
    """
        降速
    """

    def __init__(self, value):
        self.value = value

    def impact(self):
        print("降低%s速度" % self.value)