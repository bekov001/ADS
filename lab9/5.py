import sys

def lps_last(s: str) -> int:
    lps = [0]*len(s)
    j = 0
    for i in range(1, len(s)):
        while j and s[i] != s[j]:
            j = lps[j-1]
        if s[i] == s[j]:
            j += 1
        lps[i] = j
    return lps[-1] if s else 0

it = iter(sys.stdin.read().strip().split())
t = int(next(it))
out = []
for _ in range(t):
    s = next(it)
    k = int(next(it))
    n = len(s)
    lp = lps_last(s)
    ans = n + (k-1)*(n - lp)
    out.append(str(ans))
print("\n".join(out))
