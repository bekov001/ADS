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

t = int(input())
for _ in range(t):
    words = input().split()
    items = [(len(w), i, w) for i, w in enumerate(words)]
    items = mergesort(items, key=lambda x: (x[0], x[1]))

    print(*[w for _, _, w in items])