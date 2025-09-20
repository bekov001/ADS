import math

n = int(input())
if n == 1:
    print("NO")
    exit()

for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        print("NO")
        break
else:
    print("YES")