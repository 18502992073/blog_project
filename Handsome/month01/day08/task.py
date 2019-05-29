"""
作业4：定义方法,根据成绩判断等级。
       0---100   优秀  良好  及格  不及格
"""


def get_score_level(target_score):
    """
    根据成绩判断等级,0---100   优秀  良好  及格  不及格
    :param target_score:
    :return:
    """
    if target_score < 1 or target_score > 100:
        return None
    if target_score > 95:
        return "优秀"
    if target_score > 85:
        return "良好"
    if target_score > 60:
        return "及格"
    return "不及格"


print(get_score_level(86))

"""
扩展作业：定义方法，计算指定范围内的素数。
		1  -- 100
"""


def is_prime(number):
    if number < 2:
        return False
    for j in range(2, number):
        if number % j == 0:
            return False
    else:
        return True


def get_prime_number(begin, end):
    return [number for number in range(begin, end + 1) if is_prime(number)]


print(get_prime_number(1, 20))
