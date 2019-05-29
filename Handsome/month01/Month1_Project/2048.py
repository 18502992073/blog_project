def zero_to_end(list_target):
    """
    将列表中0元素，移动到末尾，其余依次往前排
    :param list_target:
    :return:
    """
    # list_result = []
    # for item in list_target:
    #     if item != 0:
    #         list_result.append(item)
    list_result = [item for item in list_target if item != 0]
    list_result +=[0]* list_target.count(0)
    list_target[:]= list_result[:]


def merge(list_target):
    """
    合并相同（不相邻也可以）列表元素的函数
    :param list_target:
    :return:
    """
    zero_to_end(list_target)
    for i in range(len(list_target) - 1):
        if list_target[i] != 0 and list_target[i] == list_target[i + 1]:
            list_target[i] += list_target[i + 1]
            list_target[i + 1] = 0
    zero_to_end(list_target)



def print_atlas(list_atlas):
    """
    在控制台中绘制2048的地图
    :param list_atlas:
    :return:
    """
    for r in range(len(list_atlas)):
        for c in range(len(list_atlas[r])):
            print(list_atlas[r][c], end=" ")
        print()


def move_up(list_atlas):
    """
    将二维列表每列元素形成一维列表,交给合并merge函数向上合并,再还给二维列表
    :param list_atlas:
    :return:
    """
    for c in range(len(list_atlas)):
        list = []
        for r in range(len(list_atlas)):
            list.append(list_atlas[r][c])
        merge(list)
        for r in range(len(list_atlas)):
            list_atlas[r][c] = list[r]



def move_left(list_atlas):
    """
    将二维列表每行元素形成一维列表,交给合并merge函数向左合并,再还给二维列表
    :param list_atlas:
    :return:
    """
    for r in range(len(list_atlas)):
        merge(list_atlas[r])


def move_down(list_atlas):
    """
    将二维列表每列元素形成一维列表,交给合并merge函数向下合并,再还给二维列表
    :param list_atlas:
    :return:
    """
    for c in range(len(list_atlas)):
        list = []
        for r in range(len(list_atlas)):
            list.append(list_atlas[-1 - r][c])
        merge(list)
        for r in range(len(list_atlas)):
            list_atlas[r][c] = list[-1 - r]



def move_right(list_atlas):
    """
    将二维列表每行元素形成一维列表,交给合并merge函数向右合并,再还给二维列表
    :param list_atlas:
    :return:
    """
    for r in range(len(list_atlas)):
        list = []
        for c in range(len(list_atlas)):
            list.append(list_atlas[r][-1 - c])
        merge(list)
        for c in range(len(list_atlas)):
            list_atlas[r][c] = list[-1 - c]



a = [[2, 0, 2, 2],
     [2, 2, 0, 2],
     [4, 4, 0, 4],
     [2, 4, 4, 0]]
move_up(a)
print_atlas(a)
