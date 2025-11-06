import sys
s = sys.stdin.readline().rstrip('\n')
n = len(s)

MOD1, MOD2 = 1_000_000_007, 1_000_000_009
B1, B2 = 911382323, 972663749

p1 = [1]*(n+1); p2 = [1]*(n+1)
for i in range(1, n+1):
    p1[i] = (p1[i-1]*B1) % MOD1
    p2[i] = (p2[i-1]*B2) % MOD2

h1 = [0]*(n+1); h2 = [0]*(n+1)
for i, ch in enumerate(s, 1):
    v = ord(ch)
    h1[i] = (h1[i-1]*B1 + v) % MOD1
    h2[i] = (h2[i-1]*B2 + v) % MOD2

def get_hash(l, r):
    x1 = (h1[r] - h1[l]*p1[r-l]) % MOD1
    x2 = (h2[r] - h2[l]*p2[r-l]) % MOD2
    return (x1, x2)

seen = set()
for i in range(n):
    for j in range(i+1, n+1):
        seen.add(get_hash(i, j))

print(len(seen))
