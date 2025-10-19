def mergesort(a):
    if len(a) <= 1:
        return a
    m = len(a) // 2
    L = mergesort(a[:m])
    R = mergesort(a[m:])
    return merge(L, R)

def merge(L, R):
    i = j = 0
    res = []
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            res.append(L[i]); i += 1
        else:
            res.append(R[j]); j += 1
    if i < len(L): res.extend(L[i:])
    if j < len(R): res.extend(R[j:])
    return res

import sys
data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
arr = mergesort(data[1:1+n])

min_diff = min(arr[i+1] - arr[i] for i in range(n-1))
out = []
for i in range(n-1):
    d = arr[i+1] - arr[i]
    if d == min_diff:
        out.extend([arr[i], arr[i+1]])
print(*out)