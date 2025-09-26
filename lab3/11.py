import sys

data = list(map(int, sys.stdin.read().strip().split()))
if not data:
    sys.exit(0)

it = iter(data)
n = int(next(it)); S = int(next(it))
a = [int(next(it)) for _ in range(n)]

best = n + 1
cur = 0
l = 0

for r in range(n):
    cur += a[r]
    while cur >= S:
        if r - l + 1 < best:
            best = r - l + 1
        cur -= a[l]
        l += 1

print(best)
