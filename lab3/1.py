import sys

data = sys.stdin.read().strip().split()
if not data:
    exit()

it = iter(data)

t = int(next(it))
queries = [int(next(it)) for _ in range(t)]

n, m = int(next(it)), int(next(it))

matrix = []
pos = {}
for i in range(n):
    row = []
    for j in range(m):
        val = int(next(it))
        row.append(val)
        pos[val] = (i, j)
    matrix.append(row)

for q in queries:
    if q in pos:
        print(pos[q][0], pos[q][1])
    else:
        print(-1)
