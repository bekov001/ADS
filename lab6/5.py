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


n,m = map(int, input().split())

rows = [[] for _ in range(m)]

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        rows[j].append(row[j])

# ro = rows.copy()
for i in range(m):
    rows[i] = mergesort(rows[i], key=lambda x: -x)

for i in range(n):
    # data = []
    for j in range(m):
        print(rows[j][i], end=" ")
    print()
    # print(*data )

