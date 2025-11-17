import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    it = iter(data)
    m = int(next(it))
    n = int(next(it))

    grid = [[0] * n for _ in range(m)]
    q = deque()
    mushrooms = 0

    for i in range(m):
        for j in range(n):
            val = int(next(it))
            grid[i][j] = val
            if val == 2:
                q.append((i, j))
            elif val == 1:
                mushrooms += 1


    if mushrooms == 0:
        print(0)
        return


    minutes = 0
    dirs = (-1, 0, 1, 0, -1)


    while q and mushrooms > 0:

        for _ in range(len(q)):
            x, y = q.popleft()
            for k in range(4):
                nx = x + dirs[k]
                ny = y + dirs[k + 1]
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    mushrooms -= 1
                    q.append((nx, ny))

        if q:
            minutes += 1


    if mushrooms > 0:
        print(-1)
    else:
        print(minutes)


main()
