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


n = int(input())

old_to_new = {}
revers = {}

for i in range(n):
    old, new = (input().split())

    if old in revers:
        head = revers.pop(old)
        old_to_new.pop(head, None)
    else:
        head = old

    if new in revers:
        head2 = revers.pop(new)
        old_to_new.pop(head2, None)

    revers[new] = head
    old_to_new[head] = new

print(len(old_to_new))
for (key, value) in mergesort(list(old_to_new.items()), lambda x: x[0]):
    print(key, value)