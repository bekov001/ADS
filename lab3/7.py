import sys

data = list(map(int, sys.stdin.read().strip().split()))
if not data:
    sys.exit(0)

it = iter(data)
n = int(next(it)); k = int(next(it))
a = [int(next(it)) for _ in range(n)]

lo, hi = 1, max(a)

def flights(cap):
    s = 0
    for x in a:
        s += (x + cap - 1) // cap
        if s > k:
            return s
    return s

while lo < hi:
    mid = (lo + hi) // 2
    if flights(mid) <= k:
        hi = mid
    else:
        lo = mid + 1

print(lo)
