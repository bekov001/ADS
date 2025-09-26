import sys
from bisect import bisect_left

data = list(map(int, sys.stdin.read().strip().split()))
if not data:
    sys.exit(0)

it = iter(data)
n = int(next(it)); m = int(next(it))
a = [int(next(it)) for _ in range(n)]

pref = [0]*n
s = 0
for i, v in enumerate(a):
    s += v
    pref[i] = s

out = []
for _ in range(m):
    x = int(next(it))
    idx = bisect_left(pref, x)
    out.append(str(idx + 1))

print("\n".join(out))
