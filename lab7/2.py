from collections import deque


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
            result.append(left.popleft())
        else:
            result.append(right.popleft())
    result.extend(left)
    result.extend(right)
    return result


n1 = int(input())
arr1 = deque(map(int, input().split()))
n2 = int(input())
arr2 = deque(map(int, input().split()))

print(*merge(arr1, arr2, lambda x: x))
