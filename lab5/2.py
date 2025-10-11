import heapq

n = int(input())
array = list(map(int, input().split()))

pq = [-x for x in array]
heapq.heapify(pq)

total = 0
while len(pq) > 1:
    a = -heapq.heappop(pq)
    b = -heapq.heappop(pq)
    if a != b:
        heapq.heappush(pq, -(a - b))

print(0 if not pq else -pq[0])