"""顺序查找
    扑克牌只取红桃花色13张，用数字1-13表示。
    洗牌后，所有牌反面朝上排成一排，找出红桃7，怎么找？
    要求：若未找到输出“查找失败”；若找到输出“查找成功，是第X张牌”。
"""


# 原始数据
# [12, 10, 1, 3, 5, 7, 9, 2, 4, 6, 8, 11, 13]
def linear(value, key):
    for i in range(len(value)):
        # 对比取出数据与待查找数据
        if valve[i] == key:
            # 查找成功，返回当前下标值
            return i
    # 查找完所有数据，仍未找到
    # 返回非法下标值
    return -1

if __name__ == "__main__":
    # 原始数据valve
    valve = [12, 10, 1, 3, 5, 7, 9, 2, 4, 6, 8, 11, 13]
    # 待查找数据key=7
    key = 7
    # 调用查找函数
    res = linear(valve, key)
    if res == -1:
        print("查找失败")
    else:
        print("查找成功:", res)
