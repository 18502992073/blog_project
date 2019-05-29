# 练习：定义函数，将列表中0元素，移动到末尾。
# [2,0,2,0]   -->  [2,2,0,0]
# [0,4,2,4]   -->  [4,2,4,0]

# 适合零基础同学
# def zero_to_end(list_target):
#     # 选出非零元素 形成新列表
#     # [2, 0, 2, 0] -->  [2, 2]
#     new_list = []
#     for item in list_target:
#         if item != 0:
#             new_list.append(item)
#             # 追加零元素 [2, 2] --> [2,2,0,0]
#     # 判断原列表零元素数量： list_target.count(0)
#     for i in range(list_target.count(0)):
#         new_list.append(0)
#         # 返回新列表
#     return new_list


# def zero_to_end(list_target):
#     # 选出非零元素 形成新列表
#     # [2, 0, 2, 0] -->  [2, 2]
#     new_list = [item for item in list_target if item != 0]
#     # 重复生成零元素 [0] * list_target.count(0)
#     new_list += [0] * list_target.count(0)
#     # 返回新列表
#     return new_list

def zero_to_end(target_list):
    new_list = [i for i in target_list if i != 0]
    new_list += [0] * target_list.count(0)
    return new_list


def merge(target_list):
    target_list = zero_to_end(target_list)
    for i in range(len(target_list) - 1):
        if target_list[i] != 0 and target_list[i] == target_list[i + 1]:
            target_list[i] += target_list[i + 1]
            target_list[i + 1] = 0
    return zero_to_end(target_list)


def print_atlas(list_atlas):
    # 00   01   02   03
    for r in range(len(list_atlas)):
        for c in range(len(list_atlas[r])):
            print(list_atlas[r][c], end=" ")
        print()


atlas01 = [
    [2, 0, 0, 2],
    [8, 0, 4, 4],
    [2, 2, 0, 4],
    [0, 2, 4, 0],
]


def move_up(target_list):
    for c in range(4):
        list_merge = []
        for r in range(4):
            list_merge.append(target_list[r][c])
        list_merge = merge(list_merge)
        for r in range(4):
            target_list[r][c] = list_merge[r]
    return target_list


re = move_up(atlas01)
print_atlas(re)
