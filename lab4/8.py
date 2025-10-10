n = int(input())
arr = list(map(int, input().split()))

arr.sort()
suf = []
run = 0

for x in reversed(arr):
    run += x
    suf.append(run)

print(*suf)
