s, k = input().split()
k = int(k)
t = input().strip()

print("YES" if t.count(s) >= k else "NO")