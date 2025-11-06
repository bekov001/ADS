import sys
input = sys.stdin.readline

MOD1, MOD2 = 1_000_000_007, 1_000_000_009
B1, B2 = 911_382_323 % MOD1, 972_663_749 % MOD2

def hash_str(t):
    a1 = a2 = 0
    for ch in t:
        c = ord(ch) - 96
        a1 = (a1 * B1 + c) % MOD1
        a2 = (a2 * B2 + c) % MOD2
    return (a1, a2)

while True:
    line = input().strip()
    if not line:
        continue
    n = int(line)
    if n == 0:
        break

    pats = [input().strip() for _ in range(n)]
    T = input().strip()
    N = len(T)


    p1 = [1]*(N+1); p2 = [1]*(N+1)
    h1 = [0]*(N+1); h2 = [0]*(N+1)
    for i, ch in enumerate(T, 1):
        c = ord(ch) - 96
        p1[i] = (p1[i-1] * B1) % MOD1
        p2[i] = (p2[i-1] * B2) % MOD2
        h1[i] = (h1[i-1] * B1 + c) % MOD1
        h2[i] = (h2[i-1] * B2 + c) % MOD2

    def get_hash(l, r):
        x1 = (h1[r+1] - h1[l] * p1[r-l+1]) % MOD1
        x2 = (h2[r+1] - h2[l] * p2[r-l+1]) % MOD2
        return (x1, x2)

    freq = []
    maxf = 0
    for pat in pats:
        m = len(pat)
        if m == 0 or m > N:
            freq.append(0)
            continue
        ht = hash_str(pat)
        cnt = 0
        for l in range(0, N - m + 1):
            if get_hash(l, l + m - 1) == ht:
                cnt += 1
        freq.append(cnt)
        if cnt > maxf:
            maxf = cnt


    print(maxf)
    for pat, f in zip(pats, freq):
        if f == maxf:
            print(pat)