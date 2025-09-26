import sys
from bisect import bisect_left

data = sys.stdin.read().strip().split()
if not data:
    sys.exit(0)

n = int(data[0])
arr = list(map(int, data[1:1+n]))
x = int(data[1+n])

# бинарный поиск
idx = bisect_left(arr, x)
if idx < n and arr[idx] == x:
    print("Yes")
else:
    print("No")
