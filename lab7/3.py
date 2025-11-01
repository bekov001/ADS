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

n, m = map(int, input().split())

if n > 0:
    a = list(map(int, input().split()))
else:
    a = []
if m > 0:
    b = list(map(int, input().split()))
else:
    b = []

a = mergesort(deque(a))
b = mergesort(deque(b))


i = j = 0
res = []

while i < n and j < m:
    if a[i] == b[j]:
        res.append(a[i])
        i += 1
        j += 1
    elif a[i] < b[j]:
        i += 1
    else:
        j += 1

print(*res)
