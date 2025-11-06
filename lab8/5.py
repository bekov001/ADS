
import sys

data = list(map(int, sys.stdin.read().strip().split()))
n = data[0]
p = data[1:1+n]

res = []
prev = 0
for i in range(n):
    diff = p[i] - prev
    val = diff // (1 << i)
    res.append(chr(97 + val))
    prev = p[i]

print(''.join(res))
