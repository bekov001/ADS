import sys
input = sys.stdin.readline


q_line = input()
while q_line is not None and q_line.strip() == "":
    q_line = input()
q = int(q_line) if q_line else 0

cnt = {}
out = []

for _ in range(q):
    parts = []
    while len(parts) < 2:
        line = input()
        if not line:
            break
        toks = line.split()
        if not toks:
            continue
        parts += toks

    if len(parts) < 2:

        break

    op, x = parts[0], int(parts[1])

    if op == "insert":
        cnt[x] = cnt.get(x, 0) + 1
    elif op == "delete":
        c = cnt.get(x, 0)
        if c > 1:
            cnt[x] = c - 1
        elif c == 1:
            cnt.pop(x)
    else:
        out.append(str(cnt.get(x, 0)))

sys.stdout.write("\n".join(out))
