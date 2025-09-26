import sys
data = sys.stdin.read().strip().split()
it = iter(data)
T = int(next(it))
out_lines = []
for _ in range(T):
    N = int(next(it))
    from collections import deque
    cnt = [0]*26
    q = deque()
    out = []
    for _ in range(N):
        c = next(it)[0]
        idx = ord(c)-97
        cnt[idx] += 1
        q.append(c)
        while q and cnt[ord(q[0])-97] > 1:
            q.popleft()
        out.append(q[0] if q else "-1")
    out_lines.append(" ".join(out) + " ")
sys.stdout.write("\n".join(out_lines))