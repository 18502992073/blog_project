class ListHelper:
    """
        列表助手类
    """

    @staticmethod
    def find_all(list_target, func_condition):
        """
            查找所有满足条件的对象
        :param list_target: 对象列表
        :param func_condition: 条件
        :return:
        """
        for item in list_target:
            if func_condition(item):
                yield item

    @staticmethod
    def find_one(list_target, func_condition):
        """
            查找第一个满足条件的对象
        :param list_target: 对象列表
        :param func_condition: 条件
        :return:
        """
        for item in list_target:
            if func_condition(item):
                return item

    @staticmethod
    def get_count(list_target, func_condition):
        """
            统计满足条件的对象数量
        :param list_target: 对象列表
        :param func_condition: 条件
        :return:
        """
        int_count = 0
        for item in list_target:
            if func_condition(item):
                int_count += 1
        return int_count

    @staticmethod
    def get_max_value(list_target, func_condition):
        """
            获取最大值
        :param list_target: 对象列表
        :param func_condition:
        :return:
        """
        value_max = list_target[0]
        for i in range(len(list_target)):
            if func_condition(value_max) < func_condition(list_target[i]):
                value_max = list_target[i]
        return value_max

    @staticmethod
    def get_min_value(list_target, func_condition):
        """
            获取最小值
        :param list_target: 对象列表
        :param func_condition:
        :return:
        """
        value_min = list_target[0]
        for i in range(len(list_target)):
            if func_condition(value_min) > func_condition(list_target[i]):
                value_min = list_target[i]
        return value_min

    @staticmethod
    def sum(list_target, func_condition):
        """
            满足条件对象的累加
        :param list_target: 对象列表
        :param func_condition:
        :return:
        """
        sum_value = 0
        for item in list_target:
            sum_value += func_condition(item)
        return sum_value

    @staticmethod
    def select(list_target, func_condition):
        """
            筛选满足条件的对象
        :param list_target: 对象列表
        :param func_condition:
        :return:
        """
        for item in list_target:
            yield func_condition(item)

    @staticmethod
    def order_by(list_target, func_condition):
        """
            按条件升序排列
        :param list_target:　对象列表
        :param func_condition:　排序条件
        :return:
        """
        new_list = list_target[:]
        for i in range(len(list_target) - 1):
            for j in range(i + 1, len(list_target)):
                if func_condition(new_list[i]) > func_condition(new_list[j]):
                    new_list[i], new_list[j] = new_list[j], new_list[i]
        return new_list

    @staticmethod
    def order_by_down(list_target, func_condition):
        """
            按条件降序排列
        :param list_target:　对象列表
        :param func_condition:　排序条件
        :return:
        """
        new_list = list_target[:]
        for i in range(len(list_target) - 1):
            for j in range(i + 1, len(list_target)):
                if func_condition(new_list[i]) < func_condition(new_list[j]):
                    new_list[i], new_list[j] = new_list[j], new_list[i]
        return new_list

    @staticmethod
    def delete(list_target,func_condition):
        """
            根据条件删除所有满足条件的对象
        :param list_target:     对象列表
        :param func_condition:  删除条件
        :return:
        """
        new_list=list_target[:]
        for item in new_list:
            if func_condition(item):
                list_target.remove(item)
        return list_target




