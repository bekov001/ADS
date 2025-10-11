import heapq


n, m = map(int, input().split())
array = list(map(int, input().split()))


neg = [-x for x in array]
heapq.heapify(neg)


total = 0
while len(neg) > 0 and m > 0:
    value = -heapq.heappop(neg)
    m -= 1
    total += value
    if value > 0:
        heapq.heappush(neg, -(value - 1) )

print(total)