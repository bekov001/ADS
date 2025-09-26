import sys
from bisect import bisect_right

data = list(map(int, sys.stdin.read().strip().split()))
if not data:
    sys.exit(0)

it = iter(data)
n = int(next(it))
a = [int(next(it)) for _ in range(n)]
q = int(next(it))
queries = [int(next(it)) for _ in range(q)]

a.sort()
pref = [0]*(n+1)
for i in range(n):
    pref[i+1] = pref[i] + a[i]

out = []
for x in queries:
    idx = bisect_right(a, x)   # сколько ≤ x
    out.append(f"{idx} {pref[idx]}")

print("\n".join(out))
