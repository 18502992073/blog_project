def print_rectangle(number01, number02, char):
    """
    打印矩形
    :param number01: 打印行数，整型
    :param number02: 打印列数，整型
    :param char: 要打印的字符
    :return: 对应行列数的矩形
    """
    for i in range(number01):
        for j in range(number02):
            print(char, end="")
        print()


# n, m = int(input("输入行数")), int(input("输入列数"))
# char="+"
# print_rectangle(n, m,char)

def judge(list):
    """
    判断列表元素是否有相同
    :param list:列表类型
    :return: 判断结果
    """
    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            if list[i] == list[j]:
                return True
    return False


ls = [1, 4, 8, 8]


# print(judge(ls))

def judge_season(month):
    """
    输入月份判断是那个季节
    :param month: 月份，整数
    :return: 季节
    """
    if 1 > month or month > 12:
        return None
    if month <= 3:
        return "春天"
    if month <= 6:
        return "夏天"
    if month <= 9:
        return "秋天"
    return "冬天"


# month = 5
# print(judge_season(month))


def get_chinese_char_count(str_target):
    """
    判断字符串中中文的个数．
    :param str_target: 要判断的字符串
    :return: 汉字的个数
    """
    count = 0
    for char in str_target:
        if 0x4E00 <= ord(char) <= 0x9FA5:
            count += 1
    return count


# s = "16864kjh你叫南湖好"
# print(get_chinese_char_count(s), "个汉字")


def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
def get_day_by_month(year, month):
    """

    :param year:
    :param month:
    :return:
    """
    if 1 > month or month > 12:
        return 0
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if month in (4, 6, 9, 11):
        return 30
    if is_leap_year(year):
        return 29
    return 28

# print(get_day_by_month(2016,2))

def zero_to_end(list_target):
    for i in list_target:
        if i==0:
            list_target.remove(i)
            list_target.append(0)
    return list_target
s=[0,1,2,0,5,0,0,4,3,0]
print(zero_to_end(s))


