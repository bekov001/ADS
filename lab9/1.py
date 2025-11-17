import sys, math

A = sys.stdin.readline().rstrip('\n')
B = sys.stdin.readline().rstrip('\n')

k = math.ceil(len(B) / len(A)) if A else 0
s = A * k
if B in s:
    print(k)
elif B in s + A:
    print(k + 1)
else:
    print(-1)
