from collections import deque

n = int(input().strip())
line = input().strip()

qk = deque()
qs = deque()
for idx, c in enumerate(line):
    if c == "K":
        qk.append(idx)
    else:
        qs.append(idx)

while qk and qs:
    k = qk.popleft()
    s = qs.popleft()
    if k < s:
        qk.append(k + n)
    else:
        qs.append(s + n)

print("KATSURAGI" if qk else "SAKAYANAGI")