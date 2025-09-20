n = int(input())
data = list(map(int, input().split()))

k = int(input())


num = -134345643564323456
minim = 1234567890123456789
index = 0
for ind, el in enumerate(data):
    if abs(el - k) < minim:
        minim = abs(el - k)
        num = el
        index = ind

print(index)