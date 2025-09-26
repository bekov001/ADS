import sys

data = list(map(int, sys.stdin.read().strip().split()))
if not data:
    sys.exit()

it = iter(data)
n = int(next(it)); H = int(next(it))
bags = [int(next(it)) for _ in range(n)]

lo, hi = 1, max(bags)

def can(k):
    hours = 0
    for x in bags:
        hours += (x + k - 1) // k  # ceil(x / k)
        if hours > H:
            return False
    return True

while lo < hi:
    mid = (lo + hi) // 2
    if can(mid):
        hi = mid
    else:
        lo = mid + 1

print(lo)
