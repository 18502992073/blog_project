def sequentialsearch(target, key):
    for i in range(len(target)):
        if target[i] == key:
            return i
    return -1


def binarysearch(target, key, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    if target[middle] > key:
        return binarysearch(target, key, left, middle-1)
    elif target[middle] < key:
        return binarysearch(target, key, middle+1, right)
    else:
        return middle


def binarysearchloop(target, key):
    left = 0
    right = len(value)-1
    while left <= right:
        middle = (left + right)//2
        if target[middle] == key:
            return middle
        elif target[middle] > key:
            right = middle-1
        else:
            left = middle+1
    return -1


def bubblesort(target):
    for i in range(len(target)):
        flag = False
        for j in range(len(target)-1-i):
            if target[j+1] < target[j]:
                target[j+1], target[j] = target[j], target[j+1]
                flag = True
        if not flag:
            break
    return target


def insert(target):
    for i in range(1, len(target)):
        pull = target[i]
        pos = i
        for j in range(i-1, -1, -1):
            if target[j] > pull:
                target[i] = target[j]
                pos = j
        target[pos] = pull
    return target


def quick(target):
    if len(target) < 2:
        return target
    key = target[0]
    m = [x for x in target if x > key]
    s = [s for s in target if s < key]
    e = [e for e in target if e == key]
    return quick(s) + e + quick(m)



value = [1, 5, 6, 3, 1, 2, 8, 49, 3, 4]
# print(sequentialsearch(value, 49))
# print(binarysearch(value, 8, 0, len(value)-1))
# print(binarysearchloop(value, 8))
# print(bubblesort(value))
# print(insert(value))
print(quick(value))



