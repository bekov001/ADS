import sys
from bisect import bisect_left, bisect_right

data = list(map(int, sys.stdin.read().strip().split()))
if not data:
    sys.exit()

it = iter(data)
n = int(next(it))
q = int(next(it))
arr = [int(next(it)) for _ in range(n)]
arr.sort()

def count_in_range(L, R):
    if L > R:
        L, R = R, L
    return bisect_right(arr, R) - bisect_left(arr, L)

out = []
for _ in range(q):
    l1 = int(next(it)); r1 = int(next(it)); l2 = int(next(it)); r2 = int(next(it))
    if l1 > r1: l1, r1 = r1, l1
    if l2 > r2: l2, r2 = r2, l2
    c1 = count_in_range(l1, r1)
    c2 = count_in_range(l2, r2)
    L = max(l1, l2); R = min(r1, r2)
    inter = count_in_range(L, R) if L <= R else 0
    out.append(str(c1 + c2 - inter))

print("\n".join(out))
