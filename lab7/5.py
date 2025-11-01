from collections import deque
from itertools import  islice


def mergesort(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # print(mid)
    left = deque(islice(arr, 0, mid))
    right = deque(islice(arr, mid, len(arr)))
    return merge(mergesort(left, key), mergesort(right, key), key)


def merge(left, right, key):
    left = deque(left)
    right = deque(right)
    result = []
    while left and right:
        if key(left[0]) < key(right[0]):
            result.append(left.popleft())
        else:
            result.append(right.popleft())
    result.extend(left)
    result.extend(right)
    return result


n , m = map(int, input().split())






data = []
for i in range(n):
    data.append(list(map(int, input().split())))

data = mergesort(data, key=lambda row: (-sum(row), row))

for i in range(n):
    print(*data[i], end=" \n")