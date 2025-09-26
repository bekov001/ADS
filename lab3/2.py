import sys

data = list(map(int, sys.stdin.read().strip().split()))
if not data:
    sys.exit(0)

it = iter(data)
n = int(next(it))
k = int(next(it))
a = [int(next(it)) for _ in range(n)]

lo = max(a)
hi = sum(a)

def feasible(limit: int) -> bool:
    blocks = 1
    cur = 0
    for x in a:
        if cur + x > limit:
            blocks += 1
            cur = x
            if blocks > k:
                return False
        else:
            cur += x
    return True

while lo < hi:
    mid = (lo + hi) // 2
    if feasible(mid):
        hi = mid
    else:
        lo = mid + 1

print(lo)
