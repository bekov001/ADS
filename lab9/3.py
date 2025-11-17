import sys
A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

if len(A) != len(B):
    print(-1)
else:
    n = len(A)
    pos = (A + A).find(B)
    print((n - pos) % n if pos != -1 else -1)
