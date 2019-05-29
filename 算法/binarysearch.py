def binary(value, key, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    if value[middle] == key:
        return middle
    elif value[middle] < key:
        return binary(value, key, middle + 1, right)
    else:
        return binary(value, key, left, middle - 1)


value = [1, 12, 23, 24, 26]
key = 1
re = binary(value, key, 0, len(value) - 1)
print(re)
