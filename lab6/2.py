from collections import Counter

n, m = map(int, input().split())
if n == 0 or m == 0:
    print()
    exit()
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ca = Counter(a)
cb = Counter(b)

common = []
for num in ca:
    if num in cb:
        count = min(ca[num], cb[num])
        common.extend([num] * count)

print(*sorted(common))