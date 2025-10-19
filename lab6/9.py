def mergesort(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(mergesort(left, key), mergesort(right, key), key)


def merge(left, right, key):
    result = []
    while left and right:
        if key(left[0]) < key(right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result


string = input()

print(*mergesort(list(string)), sep="")