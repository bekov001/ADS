import sys

def build_prefix(s, MOD, BASE):
    n = len(s)
    h = [0] * (n + 1)
    for i, ch in enumerate(s, 1):
        h[i] = (h[i - 1] * BASE + (ord(ch) - 96)) % MOD
    return h

def get_hash(h, powb, l, r, MOD):
    return (h[r] - h[l] * powb[r - l]) % MOD

data = sys.stdin.read().splitlines()
k = int(data[0].strip())
arr = [data[i + 1].strip() for i in range(k)]
base_idx = min(range(k), key=lambda i: len(arr[i]))
arr[0], arr[base_idx] = arr[base_idx], arr[0]

MOD1, MOD2 = 1_000_000_007, 1_000_000_009
B1, B2 = 911382323, 972663749

maxn = max(len(s) for s in arr) if arr else 0
pow1 = [1] * (maxn + 1)
pow2 = [1] * (maxn + 1)
for i in range(1, maxn + 1):
    pow1[i] = (pow1[i - 1] * B1) % MOD1
    pow2[i] = (pow2[i - 1] * B2) % MOD2

pref1 = [build_prefix(s, MOD1, B1) for s in arr]
pref2 = [build_prefix(s, MOD2, B2) for s in arr]

def exists_len(L):
    if L == 0:
        return ""
    n0 = len(arr[0])
    base_set = set()
    h1, h2 = pref1[0], pref2[0]
    for i in range(0, n0 - L + 1):
        x1 = get_hash(h1, pow1, i, i + L, MOD1)
        x2 = get_hash(h2, pow2, i, i + L, MOD2)
        base_set.add((x1, x2))
    if not base_set:
        return ""
    for idx in range(1, k):
        hi1, hi2 = pref1[idx], pref2[idx]
        ni = len(arr[idx])
        if ni < L:
            return ""
        cur = set()
        for i in range(0, ni - L + 1):
            y1 = get_hash(hi1, pow1, i, i + L, MOD1)
            y2 = get_hash(hi2, pow2, i, i + L, MOD2)
            t = (y1, y2)
            if t in base_set:
                cur.add(t)
        base_set = cur
        if not base_set:
            return ""
    for i in range(0, n0 - L + 1):
        x1 = get_hash(pref1[0], pow1, i, i + L, MOD1)
        x2 = get_hash(pref2[0], pow2, i, i + L, MOD2)
        if (x1, x2) in base_set:
            return arr[0][i:i + L]
    return ""

lo, hi = 0, len(arr[0]) if arr else 0
ans = ""
while lo <= hi:
    mid = (lo + hi) // 2
    cand = exists_len(mid)
    if cand:
        ans = cand
        lo = mid + 1
    else:
        hi = mid - 1

print(ans)
