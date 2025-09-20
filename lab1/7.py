n = int(input())

visited = [False] * 8000
visited[0] = False
visited[1] = False
# visited[2] = True

res = []
for i in range(2, 8000):
    if not visited[i]:
        for j in range(i * i, 8000, i):
            if visited[j]:
                continue
            else:
                visited[j] = True
        res.append(i)

print(res[res[n - 1] - 1])