
import sys
from collections import Counter, defaultdict

s = sys.stdin.readline().strip()
n = len(s)
q = int(sys.stdin.readline())

queries = []
for _ in range(q):
    l, r = map(int, sys.stdin.readline().split())
    l -= 1
    queries.append((l, r))

# double rolling hash
MOD1, MOD2 = 1_000_000_007, 1_000_000_009
B1, B2 = 911382323, 972663749

p1 = [1]*(n+1); p2 = [1]*(n+1)
h1 = [0]*(n+1); h2 = [0]*(n+1)

for i, ch in enumerate(s, 1):
    v = ord(ch)
    p1[i] = (p1[i-1]*B1) % MOD1
    p2[i] = (p2[i-1]*B2) % MOD2
    h1[i] = (h1[i-1]*B1 + v) % MOD1
    h2[i] = (h2[i-1]*B2 + v) % MOD2

def get_hash(l, r):  # [l, r)
    x1 = (h1[r] - h1[l]*p1[r-l]) % MOD1
    x2 = (h2[r] - h2[l]*p2[r-l]) % MOD2
    return (x1, x2)


cache = {}

def ensure_len(L):
    if L in cache:
        return
    cnt = Counter()
    if L <= n:
        for i in range(0, n - L + 1):
            cnt[get_hash(i, i+L)] += 1
    cache[L] = cnt

out = []
for l, r in queries:
    L = r - l
    ensure_len(L)
    out.append(str(cache[L].get(get_hash(l, r), 0)))

print("\n".join(out))
