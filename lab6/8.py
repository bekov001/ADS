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
arr = input().split()

letter = input()

merged = mergesort(arr)

for el in merged:
    if el > letter:
        print(el)
        break

else:
    print(merged[0])
