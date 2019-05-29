class SKillDeployer:
    """
        技能释放器
    """

    def __init__(self, name):
        # 当前技能名称
        self.skill_name = name
        # 技能影响列表
        self.__impacts = []
        # 配置技能
        self.config_skill()

    def config_skill(self):
        """
            配置技能，创建技能依赖的影响效果对象
        :return:
        """
        # LowerSpeedEffect(0.8)
        # DamagedEffect(20)
        # 以后读取策划的配置文件，形成数据结构(字典的值是列表)
        dict_skill_config = {
            "降龙十八掌": ["CostSpEffect(0.8)", "DamagedEffect(20)"],
            "天下无狗": ["LowerSpeedEffect(0.8)", "DamagedEffect(20)"]
        }
        # 根据当前技能名称  获取具有的所有影响效果
        list_impact_name = dict_skill_config[self.skill_name]
        # 创建影响效果对象
        # for item in list_impact_name:
        #     self.__impacts.append(eval(item))
        self.__impacts = [eval(item) for item in list_impact_name]

    def deploy_skill(self):
        """
            释放技能
        :return:
        """
        print(self.skill_name, "释放啦")
        # 遍历技能影响列表
        for item in self.__impacts:
            # 执行影响算法
            item.impact() # 统一调用影响效果的impact方法