import sys

MOD = 1_000_000_007
BASE = 11


def get_hash(s: str) -> int:
    h = 0
    p = 1
    for c in s:
        h = (h + (ord(c) - 47) * p) % MOD
        p = (p * BASE) % MOD
    return h



n = int(input())
v = []
st = set()
for _ in range(2 * n):
    s = input().strip()
    v.append(s)
    st.add(s)

cnt = 0
for s in v:
    if cnt == n:
        break
    hs = str(get_hash(s))
    if hs in st:
        print(f'Hash of string "{s}" is {hs}')
        cnt += 1


