import sys

s = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
orig = [sys.stdin.readline().strip() for _ in range(n)]

S = s.lower()

def pref(t: str):
    p = [0]*len(t)
    for i in range(1, len(t)):
        j = p[i-1]
        while j and t[i] != t[j]:
            j = p[j-1]
        if t[i] == t[j]:
            j += 1
        p[i] = j
    return p

vals = []
best = 0
for c in orig:
    C = c.lower()
    k = pref(C + '#' + S)[-1]  
    vals.append(k)
    if k > best:
        best = k

if best == 0:
    print(0)
else:
    ans = [c for c, k in zip(orig, vals) if k == best]
    print(len(ans))
    print("\n".join(ans))
