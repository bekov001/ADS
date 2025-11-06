import sys
input = sys.stdin.readline

MOD1, MOD2 = 1_000_000_007, 1_000_000_009
B1, B2 = 911382323, 972663749

s1 = input().strip()
s2 = input().strip()
w  = input().strip()

n1, n2, m = len(s1), len(s2), len(w)
if m == 0 or min(n1, n2) < m:
    print(0)
    raise SystemExit

N = max(n1, n2)

p1 = [1]*(N+1)
p2 = [1]*(N+1)
for i in range(1, N+1):
    p1[i] = (p1[i-1]*B1) % MOD1
    p2[i] = (p2[i-1]*B2) % MOD2

def build_pref(s):
    h1 = [0]*(len(s)+1)
    h2 = [0]*(len(s)+1)
    for i, ch in enumerate(s, 1):
        o = ord(ch)
        h1[i] = (h1[i-1]*B1 + o) % MOD1
        h2[i] = (h2[i-1]*B2 + o) % MOD2
    return h1, h2

def get(h1, h2, l, r):  # hash s[l:r]
    x1 = (h1[r] - h1[l]*p1[r-l]) % MOD1
    x2 = (h2[r] - h2[l]*p2[r-l]) % MOD2
    return x1 if x1>=0 else x1+MOD1, x2 if x2>=0 else x2+MOD2

h1a, h1b = build_pref(s1)
h2a, h2b = build_pref(s2)
hw1, hw2 = build_pref(w)
target = get(hw1, hw2, 0, m)

limit = min(n1, n2) - m + 1
ans = 0
for i in range(limit):
    if get(h1a, h1b, i, i+m) == target and get(h2a, h2b, i, i+m) == target:
        ans += 1

print(ans)
