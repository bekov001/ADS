import sys
input = sys.stdin.readline

k = int(input())
arr = list(map(int, input().split()))
arr.sort()

out = []
def build(l, r):
    if l > r: return
    m = (l + r) // 2
    out.append(arr[m])
    build(l, m - 1)     
    build(m + 1, r)
build(0, len(arr) - 1)
print(*out)
