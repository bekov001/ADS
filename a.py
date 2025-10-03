# from itertools import
import itertools

a, b, c = map(int, input().split())

maxa = 0
tr = [a, b, c]
per = itertools.permutations(tr, 3)
# print(list(per))
for tr in per:
    for j in range(3):
        dp = tr[j]
        data = tr[:j] + tr[j + 1:]
        # print(data)

        for i in range(2):
            dp = max(dp * data[i], dp + data[i], dp)
        maxa = max(maxa, dp)
print(maxa)