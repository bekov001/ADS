import heapq

n = int(input())
array = list(map(int, input().split()))

heapq.heapify(array)

total = 0
for _ in range(n - 1):
    a = heapq.heappop(array)
    b = heapq.heappop(array)
    total += a + b
    heapq.heappush(array, a + b)

print(total)