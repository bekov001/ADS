import sys
import heapq

data = list(map(int, sys.stdin.read().strip().split()))
if not data:
    sys.exit(0)

it = iter(data)
n = int(next(it))
k = int(next(it))

vals = []
for _ in range(n):
    x1 = int(next(it)); y1 = int(next(it)); x2 = int(next(it)); y2 = int(next(it))
    if x1 >= 0 and y1 >= 0:
        vals.append(max(x2, y2))

if len(vals) < k:
    print(-1)
else:
    ans = heapq.nsmallest(k, vals)[-1]
    print(ans)
