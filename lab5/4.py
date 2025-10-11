import heapq


n, k = map(int, input().split())
array = list(map(int, input().split()))


neg = array.copy()
heapq.heapify(neg)

t = 0
while neg[0] < k and len(neg) > 1:
    a = heapq.heappop(neg)
    b = heapq.heappop(neg)

    heapq.heappush(neg, (a + 2 * b))
    t += 1

if len(neg) == 1 and neg[0] < k:
    print(-1)
else:
    print(t)